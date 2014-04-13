from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Model imports
from Library.models import Library, Shelf, Book

# Configure and register Library models in the admin interface
class ShelfInline(admin.TabularInline):
    model = Shelf
    extra = 0
    fields = ('shelf_code', 'max_books')
    readonly_fields = ('shelf_code', 'max_books')

    def has_add_permission(self, request):
        return False

class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    fields = ('title', 'author', 'isbn', 'condition', 'availability')
    readonly_fields = ('title', 'author', 'isbn', 'condition', 'availability')

    def has_add_permission(self, request):
        return False

class UserAdmin(admin.ModelAdmin):
    inlines = [BookInline]
 
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'shelves', 'max_shelves', 'books', 'max_books')
    search_fields = ['name']
    fieldsets = [
        ('Name',        {'fields': ['name']}),
        ('Inventory',   {'fields': [('max_shelves', 'max_books')]}),
    ]
    inlines = [ShelfInline]

    def get_formsets(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            if isinstance(inline, ShelfInline) and obj is None:
                continue
            yield inline.get_formset(request,obj)

class ShelfAdmin(admin.ModelAdmin):
    list_display = ('library', 'shelf_code', 'books', 'max_books')
    fieldsets = [
        ('Inventory', {'fields': ['library', ('shelf_code', 'max_books')]}),
    ]
    inlines = [BookInline]

    def get_formsets(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            if isinstance(inline, BookInline) and obj is None:
                continue
            yield inline.get_formset(request,obj)
    
class BookAdmin(admin.ModelAdmin):
    list_display =  ('title', 'author', 'publisher', 'genre', 'language', 'isbn', 'availability', 'condition') 
    list_filter =   ['author', 'publisher', 'genre', 'language', 'checkout_status']
    search_fields = ['title', 'author', 'publisher']
    fieldsets = [
        ('Inventory', {'fields': ['shelf', 'checkout_client', 'condition']}),
        ('Basic Information', {'fields': ['title', 'author', 'isbn']}),
        ('Details', {'fields': ['publisher', 'pub_date', 'genre', 'language']}),
    ]    

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Library,LibraryAdmin)
admin.site.register(Shelf, ShelfAdmin)
admin.site.register(Book, BookAdmin)
