from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound

from .models import Note
from .serializers import NoteSerializer


class NoteView(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


    def get_object(self):
        lookup_value = self.kwargs.get(self.lookup_field, None)
        if lookup_value is None:
            raise NotFound("Запись не найдена.")

        if lookup_value.isdigit():
            try:
                obj = self.queryset.get(pk=lookup_value)
            except Note.DoesNotExist:
                raise NotFound("Запись не найдена.")

        else:
            try:
                obj = self.queryset.get(num=lookup_value)
            except Note.DoesNotExist:
                raise NotFound("Запись не найдена.")

        obj.readed = True
        obj.save()

        return obj