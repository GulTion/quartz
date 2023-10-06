import requests
import json

url = "https://unacademy.com/api/v1/topology/notes/"

querystring = {"topology_uid":"WQZDI","feed":"notes_feed","notes_type":"pdf"}

payload = ""
headers = {"authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijg5OWVhZWM2MDIxNjhhZWNmNTM2MzRjM2ExMGRhNTljIn0.eyJ1c2VyX2lkIjoxMTA2NjI5MTYsInVpZCI6Ik41WEk1UlY4RFEiLCJkaWQiOiIiLCJqdGkiOiIxOnVhd2xZNUQ3MkxIVVR1Ykxtbm9waFN3YWl2d0ZqYyIsImV4cCI6MTY3ODE3MDY0MiwiaWF0IjoxNjc1NTc4NjQyLCJ0eXAiOjF9.HHh4eyl50H17QLrakALXf4P0h_bOp-SQl00UFWZ51hAJU0ECHkUQX9ovepCZ8AuU_4bPKt1NKeI9kJY-S6CcBTzMHzBmHn3OSDqmDtgjhZnwg10y-5cmwL-OYAnLcuTbyHXfNzJKpw2fmrD91ujZKqgAJNaqM5S2lfEptZGpRUZIc2997nF1uR7nae3nP0DWQ6Bpt5hO8T7C5xy2R7R48MctbjsH3UyiVzrPo-B3xMrKe8M4TNJo-5I5gE_KSNBldD-Jez1zxudxpRkayv_MZqAAeAuhYerAWzK19SwaWAHWKBCWVpB9t1jrzqYjcSX7qH6EBA9myWZ1smUXOSIMyA"}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

# print(response.text)

f = open("notes.json", "r")
data = json.load(f)
for i in data:
    _1 = requests.request("GET", "https://unacademy.com/api/v1/topology/child/notes/", data=payload, headers=headers, params= {"topology_uid":i['uid'],"notes_type":"pdf"}).json()
    for j in _1['children']:
        _2 = requests.request("GET", "https://unacademy.com/api/v1/topology/notes/", data=payload, headers=headers, params= {"topology_uid":j['uid'],"feed":"notes_feed","notes_type":"pdf"}).json()
        for k in _2:
            _3 = requests.request("GET", "https://unacademy.com/api/v1/topology/child/note/", data=payload, headers=headers, params= {"note_id":k['note_id']}).json()
            file = requests.get(_3["notes_url"])
            e = open(f"{i['name']} - {'_'.join(_3['name'].split('/'))}.pdf", "wb")
            e.write(file.content)
            e.close()
        



