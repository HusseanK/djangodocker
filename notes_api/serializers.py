from rest_framework import serializers
from .models import Notes


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ["title", "content"]
    #Very simple serializer