task = '''
# 1. Какие шаги ты бы предпринял, если бы пользователь сказал, что API
# возвращает ошибку 500?

# Спрошу url, информацию о пользователе и браузере/консоли/программы для доступа к API

# - Сам попроверю доступность сайта
# - Проверю мессенджер и/или email на предмет сигналов о падении веб-сервера/веб-приложения
# - Проверю логи, если я выполняю роль тех. поддержки/сис. админа или отправлю заявку в тех. поддержку

# На самом деле ошибку 500 может выкидывать и не упавший сервер, если это особая логика ответа,
# например на ddos-атаки или бан пользователя(токена), а также криворукость программиста.
# В боевом проекте должен быть супервизор поднимающий упавшее приложение/сервер.
# Также возможна недоступность API из-за высокой нагрузки(при отсутствии облачного маштабирования).

# В иных случаях, произошло нечто экстраординарное. Из разряда взлома пользовательского роутера и
# подмены dns-серверов.

'''

print(task)
