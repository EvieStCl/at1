from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FlashcardForm
from django.contrib.auth.decorators import login_required
from .models import Flashcard

def index(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'flashcards/index.html', {'flashcards': flashcards})

@login_required
def add_flashcard(request):
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Flashcard added successfully!')
            return redirect('index')
        else:
            messages.error(request, 'There was an error adding the flashcard. Please correct the errors below.')
    else:
        form = FlashcardForm()
    return render(request, 'flashcards/add_flashcard.html', {'form': form})