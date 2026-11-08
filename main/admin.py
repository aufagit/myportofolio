
from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Experience, Education


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "organization",
        "category",
        "started_at",
        "ended_at",
        "ongoing_status",
    )

    search_fields = ("title", "organization")
    list_filter = ("category",)
    ordering = ("-started_at",)

    fieldsets = (
        ("Informasi Pengalaman", {
            "fields": (
                "title",
                "organization",
                "category",
            ),
        }),

        ("Deskripsi Pekerjaan", {
            "fields": ("description",),
        }),

        ("Periode Pengalaman", {
            "fields": (
                "started_at",
                "ended_at",
            ),
            "description": (
                "Isi tanggal mulai dan selesai. "
                "Kosongkan tanggal selesai jika masih aktif."
            ),
        }),

        ("Informasi Tambahan", {
            "fields": ("thumbnail",),
            "classes": ("collapse",),
        }),
    )

    formfield_overrides = {
        models.TextField: {
            "widget": Textarea(
                attrs={"rows": 4, "cols": 85}
            ),
        },
    }

    @admin.display(
        boolean=True,
        description="Masih Berlangsung"
    )
    def ongoing_status(self, obj):
        return obj.is_ongoing


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "institution",
        "major",
        "degree_level",
        "ended_at",
    )
    search_fields = ("institution", "major")
