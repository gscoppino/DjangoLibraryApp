from django.contrib import admin

# Model imports
from Library.models import Library, Shelf, Book

# Configure and register Library models in the admin interface
class ShelfInline(admin.TabularInline):
    model = Shelf
    extra = 0
    fields = ('shelf_code', 'max_books')
    readonly_fields = ('shelf_code', 'max_books')

class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    fields = ('title', 'author', 'isbn', 'condition')
    readonly_fields = ('title', 'author', 'isbn', 'condition')

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'shelves', 'max_shelves', 'books', 'max_books')
    fieldsets = [
        ('Name',        {'fields': ['name']}),
        ('Inventory',   {'fields': ['max_shelves', 'max_books']}),
    ]
    inlines = [ShelfInline]

class ShelfAdmin(admin.ModelAdmin):
    list_display = ('library', 'shelf_code', 'books', 'max_books')
    fieldsets = [
        ('Inventory', {'fields': ['library', 'shelf_code', 'max_books']}),
    ]
    inlines = [BookInline]
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'pub_date', 'genre', 'language', 'isbn', 'condition')
    list_filter = ['author', 'publisher', 'genre', 'pub_date', 'language']
    fieldsets = [
        ('Inventory', {'fields': ['shelf', 'condition']}),
        ('Basic Information', {'fields': ['title', 'author', 'isbn']}),
        ('Details', {'fields': ['publisher', 'pub_date', 'genre', 'language']}),
    ]    

admin.site.register(Library,LibraryAdmin)
admin.site.register(Shelf, ShelfAdmin)
admin.site.register(Book, BookAdmin)
