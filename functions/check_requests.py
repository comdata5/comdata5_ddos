import requests

def check_connect():
    ip = input("Введите айпи: (буквы) " )
    response = requests.get(ip)

    if response.status_code == 200:
        print("Есть подключение!")
    elif response.status_code == 404:
        print("Недоступно!")
    else :
        print("Ошибка")
