from django.db import models


# Create your models here.
# class Library(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)


class User(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True, default=0)
    user_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_of_membership = models.DateTimeField(auto_now=True)
    number_of_books_borrowed = models.IntegerField(default=0)
    max_book_limit = models.IntegerField(default=3)
    address = models.CharField(max_length=255)
    is_signed_up = models.BooleanField(default=False)
    # library = models.ForeignKey(Library, related_name='users', on_delete=models.CASCADE)


#
# class Author(User):
#     biography = models.TextField()
#
#
class Book(models.Model):
    book_id = models.AutoField(primary_key=True, unique=True, default=0)
    STATUS = [("B", "BORROWED"), ("AV", "AVAILABLE")]
    title = models.CharField(max_length=255)
    year_published = models.DateField()
    status = models.CharField(max_length=6, choices=STATUS, default="AV")
    ISBN = models.CharField(max_length=13, unique=True)
    date_borrowed = models.DateTimeField(null=True, blank=True)
    borrower = models.ForeignKey(User, null=True, blank=True, related_name='borrowed_books',
                                 on_delete=models.SET_NULL)

    # library = models.ForeignKey(Library, related_name='books', on_delete=models.CASCADE)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, {self.year_published},{self.status}, {self.ISBN}"
