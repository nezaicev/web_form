## Web-form
Скрипт обращаеться к API сервиса [[bit.ly]](https://app.bitly.com), позволяет сдеать короткую ссылку и получить количество переходов по данной сыылке.
Для запросов используется библиотека requests.

##  Как  запустить
В системе должен быть установлен Python3

```bash
pip install -r requirements.txt
``` 

#### Переменные окружения
- BITLY_GENERIC_ACCESS_TOKEN
.env example:
```
BITLY_GENERIC_ACCESS_TOKEN=1230f4335d4fbec167abfb3c3tyu6998879a6be4
```
##### Как получить

1. Зарегистрироваться в [[bit.ly]](https://app.bitly.com)
2. Необходимо получить GENERIC ACCESS TOKEN. Для упрощения дпроцедуры используете e-mail регистрацию.

#### Запуск
Получение короткой ссылки из длинной
``` bash
$ python main.py https://test.com

# Вы получите
Короткая ссылка:  https://bit.ly/30ZKoDA
```
Получение количества просмотров
``` bash
$ python main.py https://bit.ly/30ZKoDA

# Вы получите
По вашей ссылке прошли: 5 раз(а)
```
## Цель проекта 
Практика разработки на python