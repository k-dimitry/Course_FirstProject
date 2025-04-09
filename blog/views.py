from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest


def index(request, id):
    people = [None, 'Bob', 'Sam', 'Tom']
    # если пользователь найден, возвращаем его
    if id in range(1, len(people)):
        return HttpResponse(people[id])
    # если нет, то возвращаем ошибку 404
    else:
        return HttpResponseNotFound('Not Found')


def access(request, age):
    # если возраст НЕ входит в диапазон 1-110, посылаем ошибку 400
    if age not in range(1, 111):
        return HttpResponseBadRequest('Некорректные данные')
    # если возраст меньше 18, то возвращаем ошибку 403
    if age < 18:
        return HttpResponseForbidden('Доступ заблокирован: недостаточно лет')
    # если нет, тогда доступ разрешен
    else:
        return HttpResponse('Доступ разрешен')
