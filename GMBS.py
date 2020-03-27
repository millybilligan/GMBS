
# coding: UTF-8

import os
import requests
import datetime
import checker as checker
from socket import *
from threading import Thread

openPorts = []
closedPorts = []

wordlistTrue = False
targetIP = "None" 
targetURL = "None"

def startMenu():
    '''Printing a default start menu'''
    global targetIP
    global targetURL
    print(
        '\n \
           |---------------------GMS-----------------------|\n \
           |------------Author->Milly Billigan-------------|\n \
           |--------Global Milly Billigan\'s Scanner--------|\n \
             TargetIP : ' + targetIP + '                     \n \
             TargetURL : ' + targetURL + '                   \n \
             Port :                                         \n \
           |-------------------MENU------------------------|\n \
           | 1. Select a target                            |\n \
           | 2. Select a URL                               |\n \
           | 3. Port scanning                              |\n \
           | 4. Brute Url                                  |\n \
           | 0. Exit                                       |\n \
           |-----------------------------------------------|\n'
    )

    choice = input('-->')

    if choice == '0':
        print('Thanks for using my software! \
               (c)Malchik Ethernet')
        exit()
    if choice == '1':
        targetIP = input('Enter host to scan: ')
        startMenu()
    if choice == '2':
        targetURL = input('Enter url to scan: ')
        startMenu()
    if choice == '3':
        scanning()
    if choice == '4':
        bruteUrl()

    return targetIP


def scanning():
    global targetIP
    port = input('How much ports from 0:')
    targetIP = gethostbyname(targetIP)
    print('Starting scan on host ', targetIP)

    for i in range(0, int(port)):
        s = socket(AF_INET, SOCK_STREAM)
        result = s.connect_ex((targetIP, i))
        if (result == 0):
            timeNow = datetime.datetime.today()
            print('[' + str(timeNow.strftime("%H.%M.%S")) + ']' + 'Port %d is open.' % (i,) + ' | ' + checker.checkPort(i))
            openPorts.append(i)
            s.close()
        else:
            closedPorts.append(i)

def downloadWordlist():
    os.system('mkdir /usr/share/wordlists')
    os.system('wget -P /usr/share/wordlists/ https://github.com/praetorian-code/Hob0Rules/raw/master/wordlists/rockyou.txt.gz')
    os.system('gunzip /usr/share/wordlists/rockyou.txt.gz')
    wordlistTrue = True
    

def bruteUrl():
        global targetURL
        OK200 = {}
        defaultWordlist = "/usr/share/wordlists/rockyou.txt"
        wordlist = input("Write a path to wordlist \n[Write 'install' to install rockyou.txt.gz, NEED SUDO]:")
        if wordlist == 'install':
            downloadWordlist()
            bruteUrl()
        if wordlist == '':
            print("The path to the dictionary was not entered. Starting the default dictionary...")
            try:  # Проверка наличия стандартного словаря
                file = open("/usr/share/wordlists/rockyou.txt", "r")
                wordlist = file.read().splitlines()
                for x in wordlist:
                    if requests.get(targetUrl + x) == "<Response [200]>":
                        print(targetUrl + x + " | " + "Response 200")
                        OK200.append(targetUrl.x)
                    else:
                        print("Response NOT 200")
                print(wordlist)
                pass 
                #to do
            except:
                pass
                # to do
        if wordlist != 0 and wordlist != '':
                pass
                # to do


startMenu()
