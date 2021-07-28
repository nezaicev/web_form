import requests

URL = 'http://0.0.0.0:8080/get_form'

test_params_1 = {"arrival_date": "12.03.2020",
                 "phone_number": "+79150846377",
                 "description": "Tarzan"}

test_params_2 = {"manager": "Ivan",
                 "age": 10,
                 "birth_date": "2020-12-03",
                 "teacher_number": "+79850635077",
                 "level": "1"}

test_params_3 = {"main_email": "test@mail.ru",
                 "main_phone": "+79564346345", }

test_params_4 = {
                 "birth_date": "12-04-2020", }

test_params_5 = {"main_email": "test@mail",
                 "main_phone": "879564346345", }


def get_result(url, params):
    response = requests.post(url=url, params=params)
    response.raise_for_status()
    return response.text


def main():
    print(get_result(URL,test_params_1))
    print(get_result(URL, test_params_2))
    print(get_result(URL, test_params_3))
    print(get_result(URL, test_params_4))
    print(get_result(URL, test_params_5))


if __name__ == '__main__':
    main()
