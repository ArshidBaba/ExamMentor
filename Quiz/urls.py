from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from .apiviews import CategoryList, CategoryDetail, AnswersList, UserCreate, LoginView
from .models import Questions

# schema_view = get_swagger_view(title="ExamPrep")
schema_view = get_schema_view(
    title="Exam Prep Api",
    url="http://127.0.0.1:8000/subject",
    urlconf="ExamPrep.urls"
)
# dskjfjdskfh
urlpatterns = [
    path("subject/", CategoryList.as_view(), name="subject_list"),
    # path("subject/<int:pk>/", CategoryDetail.as_view(), name="subject_detail"),
    path("questions/<int:pk>/", AnswersList.as_view(), name="answer_list"),
    path('r/<str:topic>/', CategoryDetail.as_view(), name='question_list'),
    path("users/", UserCreate.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name="login"),
    path('swagger/', schema_view),
    path('docs/', include_docs_urls(title='ExamPrep')),
    path('openapi', get_schema_view(
        title='ExamPrep',
        description="Exam Prep App",
        version="1.0.0",
    ),
    name='openapi-schema'),
]