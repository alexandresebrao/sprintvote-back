from django.urls import path
from .views import DeckList, DeckRetriveUpdateDestroy

urlpatterns = [
    path('', DeckList.as_view()),
    path('<id>', DeckRetriveUpdateDestroy.as_view()),
]