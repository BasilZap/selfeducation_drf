from selfedu.models import TestAnswer, UserTestComplete, TestQuestion
from users.models import User


def check_user_answer(data: dict, user: User) -> dict:
    """
    Функция для проверки ответов на тестовый вопрос и
    создания в БД записи, если пользователь ответил правильно
    :param data: Словарь из запроса Request -> dict
    :param user: Пользователь из запроса Request -> dict
    :return: словарь со значениями - выполнено/ошибка, правильность ответа, подсказка или сообщение об ошибке -> dict
    """
    try:
        # Делаем выборку из базы правильных ответов по вопросу пользователя
        quest_id = data['id']
        test_question = TestAnswer.objects.filter(question=quest_id, is_true=True)

        # Определяем множество для ответов пользователя
        user_ans = set()
        # Создаем множество ответов пользователя
        for j in data['answers']:
            user_ans.add(j['id'])

        # Определяем множество для правильных ответов
        right_ans = set()
        # Создаем множество правильных ответов
        for i in test_question.values_list():
            right_ans.add(i[0])

        # Сравниваем множества, если множества равны - ответ верный
        dif = right_ans.symmetric_difference(user_ans)
        if dif:
            message = {"success": True, "is_true": False, "hint": "Ответ неверный"}
        else:
            message = {"success": True, "is_true": True, "hint": "Ответ верный"}
            # Если пользователь ответил верно - создаем запись, что пользователь прошел этот тест
            test_complete = UserTestComplete.objects.get_or_create(
                user=user,
                question=TestQuestion.objects.get(pk=data['id']),
                is_done=True
            )
            new_test_complete = test_complete[0]
            new_test_complete.save()
    except KeyError:
        message = {"success": False, "hint": "Проверьте правильность наименования ключей ('id', 'answers')"}
    except TypeError:
        message = {"success": False, "hint": "Введены некорректные данные, проверьте формат записи"}
    return message
