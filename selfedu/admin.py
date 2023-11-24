from django.contrib import admin

from selfedu.models import Chapter, Material, TestQuestion, TestAnswer


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'last_update')


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('chapter', 'name', 'image', 'video', 'description', 'last_update')


@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ('material', 'question', 'hint')


@admin.register(TestAnswer)
class TestAnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'is_true')
