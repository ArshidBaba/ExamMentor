from rest_framework.views import APIView
from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.contrib.auth import authenticate
# from ExamPrep.Quiz.views import category_detail

from .models import Answers, Questions, Category
from .serializers import AnswersSerializer, CategorySerializer, QuestionsSerializer, CategoryDetailSerializer, UserSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class CategoryDetail(generics.RetrieveDestroyAPIView):
#     queryset = Questions.objects.all()
#     serializer_class = CategoryDetailSerializer


# class CategoryList(APIView):
#     def get(self, request):
#         questions = Category.objects.all()[:20]
#         data = CategorySerializer(questions, many=True).data
#         return Response(data)

class CategoryDetail(APIView):
    def get(self, request, format=None, **kwargs):
        question = Questions.objects.filter(category__name=kwargs['topic']).order_by('?')
        serializer = CategoryDetailSerializer(question, many=True)
        return Response(serializer.data)

# class AnswersList(APIView):
#     def get(self, request, format=None, **kwargs):
#         question = Questions.objects.filter()
#         data = AnswersSerializer(question).data
#         return Response(data)

class AnswersList(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP__400__BAD_REQUEST)