from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import NoteView

router = DefaultRouter()
router.register('notes', NoteView)


urlpatterns = [
    path('', include(router.urls))
]