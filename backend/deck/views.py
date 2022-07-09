from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Deck
from .serializers import DeckSerializer

# Create your views here.

class DeckList(generics.ListAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

class DeckRetriveUpdateDestroy(generics.RetrieveAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    lookup_field = 'id'
