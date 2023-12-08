from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from selfedu.models import Chapter, Material, TestQuestion, TestAnswer
from selfedu.paginators import ChapterPaginator
from selfedu.serializers import ChapterListSerializer, ChapterRetrieveSerializer, TestAnswerSerializer, \
    TestQuestionSerializer, MaterialRetrieveSerializer
from selfedu.service import check_user_answer


class ChapterListAPIView(generics.ListAPIView):
    """
    Представление списка разделов
    """
    serializer_class = ChapterListSerializer
    queryset = Chapter.objects.all().order_by('id')
    pagination_class = ChapterPaginator


class ChapterRetrieveAPIView(generics.RetrieveAPIView):
    """
    Представление для просмотра раздела
    """
    serializer_class = ChapterRetrieveSerializer
    queryset = Chapter.objects.all()


class MaterialRetrieveAPIView(generics.RetrieveAPIView):
    """
    Представление для просмотра материала
    """
    serializer_class = MaterialRetrieveSerializer
    queryset = Material.objects.all()


class TestQuestionAPIView(generics.RetrieveAPIView):
    """
    Представление для просмотра тестового вопроса
    """
    serializer_class = TestQuestionSerializer
    queryset = TestQuestion.objects.select_related('material')


class TestAnswerAPIView(generics.ListAPIView):
    """
    Представление для просмотра списка тестовых ответов
    """
    serializer_class = TestAnswerSerializer
    queryset = TestAnswer.objects.select_related('question')


@api_view(['POST'])
def check_test(request):
    """
    Представление для проверки одного теста материала
    """
    if request.data:
        # Получаем ответ пользователя
        data = dict(request.data)
        message = check_user_answer(data, request.user)
    else:
        message = {"success": False, "hint": "Запрос не содержит данных"}
    return Response(message)


@api_view(['POST'])
def check_tests(request):
    """
    Представление для проверки всех тестов материала
    """
    message_list = []
    message = {}
    if request.data:
        try:
            # Получаем ответы пользователя на все вопросы темы
            data = dict(request.data)
            # Перебор всех вопросов
            for tests in data['answers']:
                # Проверяем ответы с помощью функции check_user_answer
                checked = check_user_answer(tests, request.user)
                message_list.append({tests['id']: checked})
            message.update({'answers': message_list})
        except KeyError:
            message = {"success": False, "hint": "Проверьте правильность наименования ключей ('id', 'answers')"}
    # Отправляем пользователю сообщение о том, что запрос пустой
    else:
        message = {"success": False, "hint": "Запрос не содержит данных"}
    return Response(message)
