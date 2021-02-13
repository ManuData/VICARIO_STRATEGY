
from instapy import InstaPy
from instapy import smart_run
import csv
import time
import random
from 'file' import 'file variable'


user_name = 'user name'
pwd = 'password'

users_target = data_pau_eche_300_400.copy()

# get a session!
session = InstaPy(username=user_name, password=pwd, headless_browser=True, disable_image_load=True)


def CreateCsv(datos_user):
    csv.register_dialect('myDialect',
    quoting=csv.QUOTE_ALL,
    skipinitialspace=True)
    with open('private_users.csv', 'w') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow([datos_user])


with smart_run(session):

    lista_non_private=[]
    for name in users_target:
        try:
            target = session.grab_followers(username=name, amount=1, live_match=True, store_locally=False)
            if target:
                lista_non_private.append(name)       
        except:
            pass
    CreateCsv(lista_non_private)



















