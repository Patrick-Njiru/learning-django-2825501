from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    # Display the following properties of pets in the admin page
    list_display = ["name", "species", "breed", "age", "sex"]