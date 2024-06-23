from django.db.migrations import serializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .exception.exception import BookNotFoundException, UserNotFoundException
from .models import Book
from .models import User
from .serializers import BookSerializer, BorrowBookRequestSerializer


# Create your views here.
@api_view()
def view_all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['POST'])
def borrow_book(request):
    bookRequestSerializer = BorrowBookRequestSerializer(data=request.data)
    if bookRequestSerializer.is_valid():
        book_id = bookRequestSerializer.validated_data['book_id']
        user_id = bookRequestSerializer.validated_data['user_id']
        try:
            book = Book.objects.get(id=book_id)
        except BookNotFoundException:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            user = User.objects.get(id=user_id)
        except UserNotFoundException:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        if book.status != "AVAILABLE":
            return Response({"error": "Book already borrowed"}, status=status.HTTP_400_BAD_REQUEST)
        BorrowBookRequestSerializer.objects.create(book=book, user=user)
        book.status = "BORROWED"
        book.save()
        user.number_of_books_borrowed += 1
        user.save()
        return Response("Book borrowed successfully", status=status.HTTP_201_CREATED)
    return Response(bookRequestSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def sign_upMember(request):
    if request.method == 'POST':
        validForm = MembershipSign_upForm(request.POST)
        if validForm.is_valid():
            user_name = validForm.cleaned_data["user_name"]
            email = validForm.cleaned_data["email"]
            password = validForm.cleaned_data["password"]
            hash_password = make_password(password)
            new_user = User.objects.create(username=user_name, email=email, password=hash_password)
            new_user.save()

            return JsonResponse({"message": f"Thank you {user_name} for joining the league of people who seek more "
                                            f"knowledge"}, status=201)
        else:
            return JsonResponse({"errors": validForm.errors}, status=400)
    return JsonResponse({"message": "This endpoint only accepts POST requests"}, status=400)
