
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

# VARIBLES CONSTANTES:
strategies_combinations_1 = ['follow & unfollow','comment','like','nombrar','reaccionar historias','ver historia']
strategies_combinations_1_reduced = ['comment','like','reaccionar historias','ver historia']


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
    data = pd.concat(li, axis=0, ignore_index=True)
    return data


def df_rename_column(df): # Renombra la columna con "CSV"
    df.rename(columns={0:'CSV'},inplace=True)

# 2. Generamos tabla con los usuarios seleccionados (TARGET):
def users_target_table(df): # Genera un DataFrame en el que cada csv es un row de datos
    rtdo = []
    for user_list in df.CSV:
        rtdo = rtdo+ast.literal_eval(user_list)
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
def strategies_generation(strategies_combinations=None): # Genera un DataFrame con las estrategias. TO DO: Si las combinaciones cambian y son tuplas u otras estructuras
    df_strategies = pd.DataFrame({'STRATEGIES':strategies_combinations})
    return df_strategies


def strategy_mapping(strategy,users): # Mapeo las estrategias a usuarios y genero un DataFrame
    mapeo_estrategias = list(map(lambda x:strategy.STRATEGIES[random.randint(0,len(strategy)-1)],users.TARGET_USERS))
    df_users_strategies = pd.DataFrame({'USERS':users.TARGET_USERS,'STRATEGY':mapeo_estrategias})
    return df_users_strategies

def days_for_strategy(fecha_inicio,dias): # Asignación de días al DataFrame para ejecutar las estrategias predefinidas
# string fecha_inicio = pd.to_datetime('today').normalize(). El normalize() para no heredar el timestamp dejandolo en 0.
# int dias
    fechas = pd.date_range(fecha_inicio, periods=dias, freq="D")
    mapeo_fechas = list(map(lambda x:fechas[random.randint(0,len(fechas)-1)],df_users_strategies.USERS))
    return mapeo_fechas

def target(df,mapped_dates):
    df_target = df.copy()
    df_target['FECHAS'] = mapped_dates
    return df_target


def bot_test(df): # Objetivo generación de output para automatizar bot
    print(df.groupby(['STRATEGY']).agg({'STRATEGY':'count','USERS':lambda x: [user for user in x]}))



def export_to_csv(df,path,name_csv_file):
    return print(df.to_csv('{}{}.csv'.format(path,name_csv_file), index = False))



def test(global_variable): # Objetivo hacer print del output de una variable global. TO DO incorporar más variables.
    print(global_variable)


# EJECUCIÓN DE FUNCIONES:

#load_data(r'../2_DATA_USERS_PUBLIC_TARGET') # Cuando estaba el script de strategies.py este este path
#load_data(r'/Users/manuelvicarioperez/VICARIO_PROJECT/STRATEGY/test/TEST_PAU_ECHE/2_DATA_USERS_PUBLIC_TARGET')

data = load_data(r'/Users/manuelvicarioperez/VICARIO_PROJECT/STRATEGY/test/TEST_PAU_ECHE/2_DATA_USERS_PUBLIC_TARGET')
df_rename_column(data)
users_target_table(data)
df_users = users_target_table(data)
remove_duplicates(df_users,[73,74])
df_strategies = strategies_generation(strategies_combinations_1_reduced)
df_users_strategies = strategy_mapping(df_strategies,df_users)
mapeo_fechas = days_for_strategy(pd.to_datetime('today').normalize(),7)
df_target = target(df_users_strategies,mapeo_fechas)
export_to_csv(df_target,r'/Users/manuelvicarioperez/VICARIO_PROJECT/STRATEGY/TEST/TEST_PAU_ECHE/3_STRATEGIES/','strategies_february')
#bot_test(df_target)
#test(df_target)









