from django.forms import DateInput, ModelForm, Select, Textarea, TextInput
from main.models import Education

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution",
            "degree_level",
            "major",
            "description",
            "ended_at",
        ]
        labels = {
            "institution": "Nama Institusi",
            "degree_level": "Tingkat Gelar",
            "major": "Jurusan / Program Studi",
            "description": "Deskripsi",
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
            "ended_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }