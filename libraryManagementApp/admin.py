from django.contrib import admin

from libraryManagementApp.models import User, Book


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_name', 'date_of_membership', 'email']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('ISBN', 'Title', 'Author', 'Year_published')
    search_fields = ('Title', 'Author')
    list_filter = ('Title', 'Author', 'Year_published')
