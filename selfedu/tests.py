import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from selfedu.models import Chapter, Material, TestQuestion, TestAnswer
from users.models import User


class TestChapterCase(APITestCase):
    """
    Класс тестирования эндпоинтов разделов
    """

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)
        self.chapter = Chapter.objects.create(
            name='TestChapter',
            image=None,
            description='Some Description',
            last_update=None
        )
        self.material = Material.objects.create(
            chapter=self.chapter,
            name='TestMaterial',
            image=None,
            video=None,
            description='Test description',
            last_update=None
        )

    def test_list_chapter(self):
        """
        Метод тестирования эндпоинта просмотра списка разделов
        :return:
        """

        response = self.client.get(
            reverse('selfedu:chapters'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'id': 1,
                        'name': 'TestChapter',
                        'image': None,
                        'description': 'Some Description'
                    }
                ]
            }
        )

    def test_retrieve_chapter(self):
        """
        Метод тестирования эндпоинта просмотра раздела
        :return:
        """

        response = self.client.get(
            reverse('selfedu:chapter', args=str(self.chapter.pk)),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': 2,
                'name': 'TestChapter',
                'image': None,
                'description': 'Some Description',
                'last_update': None,
                'materials': [
                    {
                        'chapter': 2,
                        'id': 2,
                        'name': 'TestMaterial',
                        'image': None
                    }
                ]
            }
        )

    def tearDown(self):
        Chapter.objects.all().delete()
        self.chapter.delete()
        Material.objects.all().delete()
        self.material.delete()


class TestMaterialCase(APITestCase):
    """
    Класс тестирования эндпоинтов материала
    """

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)
        self.chapter = Chapter.objects.create(
            name='TestChapter',
            image=None,
            description='Some Description',
            last_update=None
        )
        self.material = Material.objects.create(
            chapter=self.chapter,
            name='TestMaterial',
            image=None,
            video=None,
            description='Test description',
            last_update=None
        )
        self.test_question = TestQuestion.objects.create(
            material=self.material,
            question='Test question'
        )

    def test_retrieve_material(self):
        """
        Метод тестирования эндпоинта просмотра материала
        :return:
        """

        response = self.client.get(
            reverse('selfedu:material', args=str(self.material.pk)),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'chapter': 3,
                'id': 3,
                'name': 'TestMaterial',
                'image': None,
                'video': None,
                'description': 'Test description',
                'last_update': None,
                'answers': [
                    {
                        'id': 1,
                        'question': 'Test question',
                        'hint': None,
                        'test_questions_done': False,
                        'answers': []
                    }
                ]
            }
        )

    def tearDown(self):
        Chapter.objects.all().delete()
        self.chapter.delete()
        Material.objects.all().delete()
        self.material.delete()
        TestQuestion.objects.all().delete()
        self.test_question.delete()


class TestQuestionTestCase(APITestCase):
    """
    Класс тестирования эндпоинтов вопросов
    """

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)
        self.chapter = Chapter.objects.create(
            name='TestChapter',
            image=None,
            description='Some Description',
            last_update=None
        )
        self.material = Material.objects.create(
            chapter=self.chapter,
            name='TestMaterial',
            image=None,
            video=None,
            description='Test description',
            last_update=None
        )
        self.test_question = TestQuestion.objects.create(
            material=self.material,
            question='Test question'
        )
        self.test_answer = TestAnswer.objects.create(
            question=self.test_question,
            answer='Test answer',
            is_true=True
        )

    def test_retrieve_test_question(self):
        """
        Метод тестирования эндпоинта просмотра тестового вопроса
        """

        response = self.client.get(
            reverse('selfedu:question', args=str(self.test_question.pk)),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        # print(response.json())
        self.assertEqual(
            response.json(),
            {
                'id': 2,
                'question': 'Test question',
                'hint': None,
                'test_questions_done': False,
                'answers': [
                    {
                        'id': 1,
                        'answer': 'Test answer'
                    }
                ]
            }
        )


class TestTestCase(APITestCase):
    """
    Класс тестирования эндпоинтов проверки вопросов
    """

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)
        self.chapter = Chapter.objects.create(
            name='TestChapter',
            image=None,
            description='Some Description',
            last_update=None
        )
        self.material = Material.objects.create(
            chapter=self.chapter,
            name='TestMaterial',
            image=None,
            video=None,
            description='Test description',
            last_update=None
        )
        self.test_question = TestQuestion.objects.create(
            material=self.material,
            question='Test question'
        )
        self.test_question2 = TestQuestion.objects.create(
            material=self.material,
            question='Test question2'
        )
        self.test_answer = TestAnswer.objects.create(
            question=self.test_question,
            answer='Test answer',
            is_true=True
        )
        self.test_answer2 = TestAnswer.objects.create(
            question=self.test_question2,
            answer='Test answer 2',
            is_true=True
        )

    def test_check_answer(self):
        data = {'id': self.test_question.pk, 'answers': [{'id': self.test_answer.pk}]}
        # print(data)

        response = self.client.post(
            reverse('selfedu:test'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'success': False, 'hint': 'Введены некорректные данные, проверьте формат записи'}
        )

    # def test_check_answers(self):
    #     data = {
    #             "answers":
    #                     [
    #                     {"id": self.test_question.pk, "answers": [{"id": self.test_answer.pk}]},
    #                     {"id": self.test_question2.pk, "answers": [{"id": self.test_answer2.pk}]}
    #                     ]
    #     }
    #
    #     print(data)
    #
    #     response = self.client.post(
    #         reverse('selfedu:tests'),
    #         data=data
    #     )
    #
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_200_OK
    #     )
    #
    #     print(response.json())
