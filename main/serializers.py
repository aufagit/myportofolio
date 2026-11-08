
from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Education


class EducationSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()
    started_at = serializers.DateTimeField(
        input_formats=["%Y-%m-%d", "iso-8601"],
        required=False
    )

    class Meta:
        model = Education
        fields = [
            "id",
            "institution",
            "degree_level",
            "major",
            "description",
            "started_at",
            "ended_at",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_institution(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Nama institusi tidak boleh kosong."
            )
        return value

    def validate_major(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Jurusan tidak boleh kosong."
            )
        return value

    def validate_description(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Deskripsi tidak boleh kosong."
            )
        return value

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False

        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(
            user.username for user in obj.starred_by.all()
        )
