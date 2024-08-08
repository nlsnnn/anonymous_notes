from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from .models import Note
from .serializers import NoteSerializer


class NoteView(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    # permission_classes = [IsAdminUser]


class NoteNumView(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'num'

    def get_object(self):
        try:
            obj = self.queryset.get(num=self.kwargs.get(self.lookup_field))
        except Note.DoesNotExist:
            raise NotFound("Note not found.")

        return obj

    def get(self, request, *args, **kwargs):
        obj  = self.get_object()
        if obj.readed:
            return Response({'detail': 'Note has been readed.'}, status=200)

        obj.readed = True
        obj.save()

        serializer = self.serializer_class(obj)
        return Response(serializer.data)