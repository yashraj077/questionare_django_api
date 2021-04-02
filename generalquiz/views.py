from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import serializers, QuestionSerializer

from .models import GeneralQuestion
from django.contrib import messages

import random


# Create your views here.
def home(request):
    return render(request, "layout.html")


def home_post(request):
    question = request.POST.get('question')
    option1 = request.POST.get('option1')
    option2 = request.POST.get('option2')
    option3 = request.POST.get('option3')
    option4 = request.POST.get('option4')
    ans = request.POST.get('ans')

    # return HttpResponse(question)
    insert = GeneralQuestion(
        question=question,
        option1=option1,
        option2=option2,
        option3=option3,
        option4=option4,
        ans=ans
    )
    insert.save()
    messages.success(request, "Question Added Successfully")
    return redirect("home")


class QuestionList(APIView):
    def get(self, request):
        questions = GeneralQuestion.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


def testurl(request):
    total_rows = GeneralQuestion.objects.all().count()
    random_id = random.randint(5, 4+total_rows)
    query = GeneralQuestion.objects.get(id=random_id)
    data = {
        'question': query.question,
        'option1': query.option1,
        'option2': query.option2,
        'option3': query.option3,
        'option4': query.option4,
        'ans': query.ans
    }
    return JsonResponse(data)
