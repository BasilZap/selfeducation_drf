from django.contrib import admin

from selfedu.models import Chapter, Material, TestQuestion, TestAnswer, UserTestComplete


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'last_update')


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'chapter', 'name', 'image', 'video', 'description', 'last_update')
    list_filter = ('chapter',)


@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'material', 'question', 'hint')
    list_filter = ('material',)


@admin.register(TestAnswer)
class TestAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'is_true')
    list_filter = ('question',)


@admin.register(UserTestComplete)
class UserTestCompleteAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'is_done')
    list_filter = ('user',)
