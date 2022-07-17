from dotenv import load_dotenv, find_dotenv
from datetime import date, datetime
from win10toast import ToastNotifier
import os
import json
import requests
import base64
import webbrowser


def BasicAuthenticator():
    load_dotenv(find_dotenv("keys.env"))
    apiUserKey = os.environ.get('HI_USER')
    apiPasswordKey = os.environ.get('HI_PWD')
    concatKey = (apiUserKey + ':' + apiPasswordKey)
    hiApiKey = base64.b64encode(str.encode(concatKey)).decode("ascii")
    headers = {'Content-Type': "application/json",
               'Authorization': "Basic %s" % hiApiKey, 'Accept': "application/json"}

    return headers


def DesktopNotify(title, msg, duration_seconds):
    # icon = "img\image3.ico"
    toaster = ToastNotifier()

    return toaster.show_toast(title, msg, threaded=False,
                              icon_path=None, duration=duration_seconds)


def GetDate():
    # Check and get date
    DAYS = ['Segunda-feira', 'Terça-feira', 'Quarta-feira',
            'Quinta-Feira', 'Sexta-feira', 'Sábado', 'Domingo']
    weekIndex = datetime.weekday(datetime.now())
    weekDay = DAYS[weekIndex]
    todayDate = date.today().strftime("%d / %m - " + weekDay)
    todayHour = datetime.now().strftime("%H:%M")

    return todayDate, todayHour


def Open_URL():
    try:
        webbrowser.open_new('www.google.com.br')
        print('Opening URL...')
    except:
        print('Failed to open URL. Unsupported variable type.')
