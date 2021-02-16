
'''

1. Descargamos los datos de path donde estén los usuarios con perfiles públicos
2. Generamos tabla con los usuarios seleccionados (TARGET)
3. Generamos tabla con estrategias en función de las combinaciones f (stage que nos encontremos)
4. Mapeo aleatoria de usuario-estrategia
5. Asignación de fecha aleatoria en función de los días que querramos aplicar la estrategia
6. Agrupación usuarios-estrategia para realización de post análisis

TO DO: Identificar las funciones que tiene que tener la clase
'''

import pandas as pd
import numpy as np
import random
import glob
import ast
import calendar

# 1. Descarga de todos datos de un path:
# NOTA: Guardar en un archivo de texto o en una lista/array para identificar lectura de paths
# sobre los que consumir los datos de usuarios con perfil público

# path = r'../2_DATA_USERS_PUBLIC_TARGET'
def load_data(path=None): # Importa los datos de un path concreto
    path = path
    all_files = glob.glob(path+'/*.csv')

    li = []
    for file in all_files:
        df = pd.read_csv(file,header=None)
        li.append(df)
    global data
    data = pd.concat(li, axis=0, ignore_index=True)
    return data


def df_rename_column(df): # Renombra la columna con "CSV"
    df.rename(columns={0:'CSV'},inplace=True)

# 2. Generamos tabla con los usuarios seleccionados (TARGET):
def users_target_table(df): # Genera un DataFrame en el que cada csv es un row de datos
    rtdo = []
    for user_list in df.CSV:
        rtdo = rtdo+ast.literal_eval(user_list)
    global df_users
    df_users = pd.DataFrame({'TARGET_USERS':rtdo})
    return df_users


# TO DO: def check_duplicates(df):

# 2.1 El output de la tabla es el DataFrame (df_users) deduplicado
def remove_duplicates(df,index_remove=None): # Elimina del DataFrame los index que se pasen por parámetro (en forma de lista)
    df.drop(index_remove,inplace=True)
    df_users = df.reset_index().drop(columns='index')
    return df_users


#3. Generamos tabla con estrategias en función de las combinaciones f (stage que nos encontremos)

strategies_combinations_1 = ['follow & unfollow','comment','like','nombrar','reaccionar historias','ver historia']
def strategies_generation(strategies_combinations=None): # Genera un DataFrame con las estrategias. TO DO: Si las combinaciones cambian.
    global df_strategies
    df_strategies = pd.DataFrame({'STRATEGIES':strategies_combinations})
    return df_strategies






# EJECUCIÓN DE FUNCIONES:

'''
#load_data(r'../2_DATA_USERS_PUBLIC_TARGET') # Cuando estaba el script de strategies.py este este path
load_data(r'/Users/manuelvicarioperez/VICARIO_PROJECT/STRATEGY/test/TEST_PAU_ECHE/2_DATA_USERS_PUBLIC_TARGET')
df_rename_column(data)
users_target_table(data)
remove_duplicates(df_users,[73,74])
strategies_generation(strategies_combinations_1)
'''






