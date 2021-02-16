
'''

1. Descargamos los datos de path donde estén los usuarios con perfiles públicos
2. Generamos tabla con los usuarios seleccionados (TARGET)
2. Generamos tabla con estrategias en función de las combinaciones f (stage que nos encontremos)
3. Mapeo aleatoria de usuario-estrategia
4. Asignación de fecha aleatoria en función de los días que querramos aplicar la estrategia
5. Agrupación usuarios-estrategia para realización de post análisis

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

    
def users_target_table(df): # Genera un DataFrame en el que cada csv es un row de datos
    rtdo = []
    for user_list in df.CSV:
        rtdo = rtdo+ast.literal_eval(user_list)
    global df_users
    df_users = pd.DataFrame({'TARGET_USERS':rtdo})
    return df_users


# TO DO: def check_duplicates(df):


# EJECUCIÓN DE FUNCIONES:

'''
load_data(r'../2_DATA_USERS_PUBLIC_TARGET')
df_rename_column(data)
users_target_table(data)
'''



