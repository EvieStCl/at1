from django.shortcuts import render
from .models import Flashcard

def index(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'flashcards/index.html', {'flashcards': flashcards})