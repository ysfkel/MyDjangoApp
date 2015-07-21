from django.shortcuts import render,get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect,HttpResponse
from .models import Question,Choice,Item
from django.core.urlresolvers import reverse
from rest_framework import generics
from myapp.serializers import ItemSerializer, QuestionSerializer

# Create your views here.

class ItemList(generics.ListCreateAPIView):
	queryset=Item.objects.all()
	serializer_class=ItemSerializer

class QuestionList(generics.ListCreateAPIView):
	queryset=Question.objects.all()
	serializer_class=QuestionSerializer
	
class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Question.objects.all()
	serializer_class=QuestionSerializer

def index(request):
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	template='myapp/index.html'
	context = {'latest_question_list': latest_question_list}
	return render(request,template,context)
	
def detail(request,question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'myapp/detail.html', {'question': question})
	
def results(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request,'myapp/results.html',{'question':question})
	
def vote(request,question_id):
	p = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice=p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request,'myapp/detail.html',{
			'question':p,
			'error_message':'You did not select a choice',
		})
	else:
		selected_choice.votes +=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('myapp:results',args=(p.id,)))
	
		
