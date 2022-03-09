from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Category, Questions, Answers

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'

    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]
        
class CategoryDetailSerializer(serializers.ModelSerializer):

    answer = AnswersSerializer(many=True, read_only=True)
    # name = QuestionsSerializer(many=True)
    # name = CategorySerializer(many=True)

    class Meta:
        model = Answers
        fields = [
             'question', 'answer',
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user