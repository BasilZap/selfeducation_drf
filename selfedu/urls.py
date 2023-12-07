from django.conf.urls.static import static
from django.urls import path

from config import settings
from selfedu.views import ChapterListAPIView, ChapterRetrieveAPIView, TestQuestionAPIView, MaterialRetrieveAPIView, \
    check_test, check_tests
from selfedu.apps import SelfeduConfig

app_name = SelfeduConfig.name

urlpatterns = [
    path('', ChapterListAPIView.as_view(), name='chapters'),
    path('chapter/<int:pk>/', ChapterRetrieveAPIView.as_view(), name='chapter'),
    path('material/<int:pk>/', MaterialRetrieveAPIView.as_view(), name='material'),
    path('question/<int:pk>/', TestQuestionAPIView.as_view(), name='question'),
    path('tests/', check_tests, name='tests'),
    path('test/', check_test, name='test'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
