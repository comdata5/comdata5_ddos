from all_func import *
ok = input("Выбери операцию!\n1.ДДос атака\n2.Проверка на подключение\n\nEnter:  ")



if ok == "2":
    check_connect()
elif ok == "1":
    ddos()
else:
    print("ОшИбо4кА")
