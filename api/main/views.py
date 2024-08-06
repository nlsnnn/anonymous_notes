from rest_framework.viewsets import ModelViewSet

from .models import Note
from .serializers import NoteSerializer


class NoteView(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer