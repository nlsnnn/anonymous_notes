from uuid import uuid4

from rest_framework.serializers import ModelSerializer

from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

    def create(self, validated_data):
        validated_data['num'] = str(uuid4())
        return super().create(validated_data)