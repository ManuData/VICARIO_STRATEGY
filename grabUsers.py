
# TEST PARA PODER COMENTAR AL USUARIO: 
# !/usr/bin/python2.7

# obtener los datos de un usuario: https://www.instagram.com/nombre_usuario/?__a=1

'''
import requests 
  
# Making a get request 
response = requests.get('http://api.github.com') 
  
# print response 
print(response) 
  
# print url 
print(response.url) 
'''
import random
from instapy import InstaPy
from instapy import smart_run
user_name = 'nombre loging'
pwd = 'password'
# LISTA DE PRUEBA: 
#test_pombo = ["nombre1","nombre2"]
users_target = ["nombre usuario target"]

# get a session!
session = InstaPy(username=user_name, password=pwd, headless_browser=True)

# let's go! :>
with smart_run(session):
    #manu_followers = session.grab_followers(username="nombre_usuario", amount="full", live_match=True, store_locally=True)
    # Usuarios que está siguiendo Maria Pombo:
    for friend in users_target:
        #target = session.grab_following(username=friend, amount="full", live_match=True, store_locally=True)
        target = session.grab_followers(username=friend, amount="full", live_match=True, store_locally=True)

