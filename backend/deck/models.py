from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Cards(models.Model):
    card = models.IntegerField()
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="cards")

    def __str__(self):
        return "%s" % (self.card)

# Create your models here.
