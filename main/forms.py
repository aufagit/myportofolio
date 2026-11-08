from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm, Select, Textarea, TextInput
from django.utils.html import strip_tags
from main.models import Education


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution",
            "degree_level",
            "major",
            "description",
            "started_at",
            "ended_at",
        ]
        labels = {
            "institution": "Nama Institusi",
            "degree_level": "Tingkat Gelar",
            "major": "Jurusan / Program Studi",
            "description": "Deskripsi",
            "started_at": "Tanggal Mulai",
            "ended_at": "Tanggal Selesai (Kosongkan jika masih berlangsung)",
        }
        widgets = {
            "institution": TextInput(
                attrs={
                    "placeholder": "Universitas Indonesia",
                }
            ),
            "major": TextInput(
                attrs={
                    "placeholder": "S1 Ilmu Komputer",
                }
            ),
            "degree_level": Select(),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pencapaian atau fokus studi...",
                    "rows": 3,
                }
            ),
            "started_at": DateInput(
                format="%Y-%m-%d",
                attrs={"type": "date"}
            ),
            "ended_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }

        # Method clean diletakkan sejajar dengan class Meta (di luar class Meta)
    def clean_institution(self):
        institution = strip_tags(self.cleaned_data.get("institution", "")).strip()
        if not institution:
            raise ValidationError("Nama institusi tidak boleh hanya berisi tag HTML.")
        return institution

    def clean_major(self):
        major = strip_tags(self.cleaned_data.get("major", "")).strip()
        if not major:
            raise ValidationError("Jurusan tidak boleh hanya berisi tag HTML.")
        return major

    def clean_description(self):
        description = strip_tags(self.cleaned_data.get("description", "")).strip()
        if not description:
             raise ValidationError("Deskripsi tidak boleh hanya berisi tag HTML.")
        return description