from django.db import models

from users.models import NULLABLE, User


# Модель "Раздел"
class Chapter(models.Model):
    name = models.CharField(max_length=300, verbose_name='Раздел')
    image = models.ImageField(upload_to='selfedu/', verbose_name='Фото', **NULLABLE)
    description = models.TextField(verbose_name='Описание раздела')
    last_update = models.DateTimeField(verbose_name='Дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


# Модель "Материал"
class Material(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name='Раздел')
    name = models.CharField(max_length=300, verbose_name='Материал')
    image = models.ImageField(upload_to='selfedu/', verbose_name='Фото', **NULLABLE)
    video = models.CharField(max_length=300, verbose_name='Ссылка на видео', **NULLABLE)
    description = models.TextField(verbose_name='Описание')
    last_update = models.DateTimeField(verbose_name='Дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name}, раздел - {self.chapter}'

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


# Модель "Тестовый вопрос"
class TestQuestion(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name='Материал')
    question = models.TextField(verbose_name='Вопрос')
    hint = models.TextField(verbose_name='Подсказка')

    def __str__(self):
        return f'{self.question}, материал - {self.material}'

    class Meta:
        verbose_name = 'Тестовый вопрос'
        verbose_name_plural = 'Тестовые вопросы'


# Модель "Вариант ответа"
class TestAnswer(models.Model):
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, verbose_name='Тестовый вопрос')
    answer = models.TextField(verbose_name='Вариант ответа')
    is_true = models.BooleanField(default=False, verbose_name='Правильный')

    def __str__(self):
        return f'Ответ {self.answer} для {self.question}'

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'


# Модель "Пройденный тест"
class UserTestComplete(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, verbose_name='Тестовый вопрос')
    is_done = models.BooleanField(default=False, verbose_name='Отвечен')
