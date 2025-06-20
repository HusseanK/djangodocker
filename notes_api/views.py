from rest_framework import viewsets

from .models import Notes
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    #Very simple REST API view