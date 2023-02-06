import time, os,sys
while True:
    os.system("cls")
    exit = input("Type exit om te stoppen :) ")
    if exit.lower() == "exit":
        os.system("cls")
        sys.exit()
    else:
        print("Dat was geen exit >:(")
        time.sleep(2)
