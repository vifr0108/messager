import requests

name = input('Введите имя: ')


while True:
    # меняем что отправлять, тестирование
    data = {
        'name': name,
        'text': input('>>> '),
    }
    response = requests.post(
        'http://127.0.0.1:5000/send',
        json=data
    )

# print(response)
# print(response.headers)
# print(response.text)
