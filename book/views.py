from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer, ReviewUpdateSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
import re
from django.conf import settings


class ReviewListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):    
        query = request.GET.get('isbn')
        if query:
            print(query)
            queryset = Review.objects.filter(book__isbn=query)
            
            if queryset.count() == 0:
                return Response({"error": "Book not found"}, status=404)
        else:
            queryset = Review.objects.all()

        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)
    
def get_book_by_isbn(isbn):
    import requests

    #realizando request a api isbn
    headers = {"Authorization": settings.ISBN_API_KEY}
    request = requests.get(f"https://api2.isbndb.com/book/{isbn}", headers=headers)

    if request.status_code == 200:
        data = request.json()
        if data and 'book' in data:
            return data['book']
    else:
        return None
    
class ReviewCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        isbn_input = request.data.get('isbn')

        # Verifica se o ISBN está presente e se corresponde ao padrão ISBN-10 ou ISBN-13
        isbn_pattern = r'^(?:\d{9}[\dXx]|\d{13})$'
        if not isbn_input or not re.match(isbn_pattern, isbn_input.replace('-', '').replace(' ', '')):
            return Response({"error": "ISBN inválido. Informe um código ISBN-10 ou ISBN-13 válido."}, status=400)

        if Review.objects.filter(isbn=isbn_input, user=request.user).exists():
            return Response({"error": "Você já possui uma avaliação ativa desse livro"}, status=400)

        book = get_book_by_isbn(isbn_input)
        if not book:
            return Response({"error": "Book not found"}, status=404)

        # Create a mutable copy of request.data
        data = request.data.copy()
        data['user'] = request.user.id

        serializer = ReviewSerializer(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

class ReviewUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        review = get_object_or_404(Review, pk=pk)
        if review.user != self.request.user:
            raise PermissionDenied("Você não tem permissão para editar esta review.")
        return review

    def patch(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewUpdateSerializer(
            review, data=request.data, partial=True, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(ReviewSerializer(review).data, status=200)


class ReviewActivationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)

        # Permissão: autor da review ou staff/superuser
        user = request.user
        if not (review.user_id == user.id or user.is_staff or user.is_superuser):
            raise PermissionDenied("Você não tem permissão para alterar o status desta review.")

        desired = request.data.get("is_active", None)
        if desired is None:
            review.is_active = not review.is_active
        else:
            review.is_active = bool(desired)

        review.save(update_fields=["is_active"])
        return Response({
            "id": review.id,
            "is_active": review.is_active
        }, status=200)
