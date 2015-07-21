from rest_framework import serializers
from myapp.models import Question, Choice,Item

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model=Question
		fields=('id','question_text','pub_date')
		
class ChoiceSerializer(serializers.ModelSerializer):
	question=QuestionSerializer()
	class Meta:
		model=Choice
		fields=('id','choice_text','votes','question')
		
class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model=Item
		fields=('id','name_text')