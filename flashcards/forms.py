from django import forms
from .models import Flashcard

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['front_side', 'back_side']

from django import forms
from django.core.validators import MaxLengthValidator
from .models import Flashcard

class FlashcardForm(forms.ModelForm):
    front_side = forms.CharField(validators=[MaxLengthValidator(100)])

    class Meta:
        model = Flashcard
        fields = ['front_side', 'back_side']