from rest_framework import serializers
from selfedu.models import Chapter, Material, TestQuestion, TestAnswer, UserTestComplete


class TestAnswerSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели ответов на тестовые вопросы
    """
    class Meta:
        model = TestAnswer
        fields = ('id', 'answer')


class TestQuestionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели тестовых вопросов
    """
    answers = TestAnswerSerializer(source='testanswer_set', many=True, read_only=True)
    test_questions_done = serializers.SerializerMethodField()

    def get_test_questions_done(self, question: TestQuestion) -> bool:
        """
        Метод определяет - проходил ли текущий пользователь этот тест
        :param question: Объект TestQuestion
        :return: наличие записи -> bool
        """
        request = self.context.get('request')
        is_done = UserTestComplete.objects.filter(user=request.user, question=question)
        if is_done:
            return True
        return False

    class Meta:
        model = TestQuestion
        fields = ('id', 'question', 'hint', 'test_questions_done', 'answers')


class MaterialListSerializer(serializers.ModelSerializer):
    """
    Сериализатор списка моделей "Материал"
    """
    class Meta:
        model = Material
        fields = ('chapter', 'id', 'name', 'image')


class MaterialRetrieveSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели "Материал"
    """
    answers = TestQuestionSerializer(source='testquestion_set', many=True, read_only=True)

    class Meta:
        model = Material
        fields = ('chapter', 'id', 'name', 'image', 'video', 'description', 'last_update', 'answers')


class ChapterListSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели "Раздел"
    """

    class Meta:
        model = Chapter
        fields = ('id', 'name', 'image', 'description')


class ChapterRetrieveSerializer(serializers.ModelSerializer):
    """
    Сериализатор для просмотра модели "Раздел"
    """
    materials = MaterialListSerializer(source='material_set', many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = ('id', 'name', 'image', 'description', 'last_update', 'materials')
