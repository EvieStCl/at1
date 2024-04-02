from django.core import serializers
from django.shortcuts import render
from .models import Question

def index(request):
    # questions = Question.objects.all()
    questions = Question.objects.order_by('?')[:2]
    questions_json = serializers.serialize('json', questions)
    return render(request, 'eduprod/index.html', {
        'questions_json': questions_json
        })

from django.core import serializers
from django.shortcuts import render
from .models import Question
from django.contrib.auth.decorators import login_required

@login_required
def index(request): 
    questions = Question.objects.all()
    # Serialize and use the JSON string directly without additional encoding
    questions_json = serializers.serialize('json', questions)
    return render(request, 'eduprod/index.html', {'questions_json': questions_json})

from django.core import serializers
from django.shortcuts import render
from .models import Question
import random

def index(request):

    # Get the first and last question ID
    first_id = Question.objects.order_by('id').first().id
    last_id = Question.objects.order_by('id').last().id
    # Initialize an array to store unique question IDs
    random_ids = []

    # Generate 5 unique random question IDs
    while len(random_ids) < 5:
        random_id = random.randint(first_id, last_id)
        # Check if the random ID matches an existing question ID and is not already in the array
        if Question.objects.filter(id=random_id).exists() and random_id not in random_ids:
            random_ids.append(random_id)

    # Retrieve the questions matching the random IDs
    questions = Question.objects.filter(id__in=random_ids)

    # Serialize the questions to JSON
    questions_json = serializers.serialize('json', questions)

    # Get distinct categories for all questions
    categories = Question.objects.values_list('category', flat=True).distinct()
    return render(request, 'eduprod/index.html', {
        'questions_json': questions_json,
        'categories': categories
    })

