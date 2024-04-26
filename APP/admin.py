from django.contrib import admin
from .models import Document, Forms, Tariff


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    search_fields = ["title", "display_title"]
    list_display = ("pk", "title", "display_title", "display_on_main_page", "created_at")
    readonly_fields = ("updated_at", "created_at",)
    date_hierarchy = "created_at"


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    search_fields = ["name", "display_title"]
    list_display = ("pk", "name", "cost", "created_at")
    readonly_fields = ("updated_at", "created_at",)
    date_hierarchy = "created_at"


@admin.register(Forms)
class FormsAdmin(admin.ModelAdmin):
    search_fields = ["title", "display_title"]
    list_display = ("pk", "__str__", "gender", "date_of_birth", "trip_number", "created_at")
    readonly_fields = ("updated_at", "created_at",)
    date_hierarchy = "created_at"
