from datetime import date, datetime
import app_data
from app_data import BasicAuthenticator as auth
import os
import json
import requests
import base64
import webbrowser


class InboxAPI:

    def __init__(self):
        pass

    def GetDepartmentsName(*args):
        # GET departments without other channels, only Inbox
        departments = 'departments'
        inboxApiGETDepartments = 'https://api.directtalk.com.br/1.5/ticket/' + departments
        response = requests.get(inboxApiGETDepartments, headers=auth())
        departmentsData = json.loads(response.content)
        departmentsNameList = []

        for i in range(len(departmentsData)):
            departmentsNameList.append(departmentsData[i]['name'])

        if response.status_code == 200:
            app_data.DesktopNotify("Sucesso!", "Foram encontrados " +
                                   str(len(departmentsNameList)) + " departamentos.", 15)
        else:
            app_data.DesktopNotify(response.status_code,
                                   "Falha ao buscar departamentos.", 15)

        return departmentsNameList


if __name__ == '__main__':
    start = InboxAPI()
    start.GetDepartmentsName()
