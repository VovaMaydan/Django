from django.http import Http404
from rest_framework import generics
from django.http import HttpResponse
from ques.models import Question, Choice
from ques.serializers import QuestionSerializer, ChoiceSerializer
from django.shortcuts import get_object_or_404

def index(request):
	question_list = Question.objects.all()
	return HttpResponse(', '.join([q.question_text for q in question_list]))

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = QuestionSerializer

    def get_object(self):
    	obj = get_object_or_404(Question, pk=self.kwargs.get('question_id'))
    	return obj

class ChoiceList(generics.ListCreateAPIView):
	queryset = Choice.objects.all()
	serializer_class = ChoiceSerializer

class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):

	serializer_class = ChoiceSerializer

	def get_object(self):
		obj = get_object_or_404(Choice, pk=self.kwargs.get('choice_id'))