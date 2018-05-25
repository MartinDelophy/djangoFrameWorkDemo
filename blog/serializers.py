from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blog.models import Question,Choice


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text','pub_date', 'text')
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Question.objects.create(**validated_data)
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.text = validated_data.get('text', instance.text)
    #     instance.question_text = validated_data.get('question_text', instance.question_text)
    #     instance.save()
    #     return instance