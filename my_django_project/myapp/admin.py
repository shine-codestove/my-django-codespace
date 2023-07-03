from django.contrib import admin

from myapp.models.person import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
    )

# Register your models here.
admin.site.register(Person, PersonAdmin)