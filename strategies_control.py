'''
OBJETIVO: Generar documento de control con las estrategias a llevar a cabo en febrero
NOTEBOOK: STRATEGIES_CONTROL

1. Cargamos los datos de las estrategias generadas para el mes x
2. Incorporamos función que permita asignar de forma aleatoria horas para la aplicación de estrategias
3. Ajustes de mañana/tarde/noche en función de las horas aleatorias asignadas
4. Descarga de excel para el control de las estrategias
'''

import pandas as pd
import random
import datetime




def lectura_datos(path=None): # Lectura de datos para el mes de febrero de las estrategias generadas
    df_february = df_february = pd.read_csv(path)
    return df_february

def random_hours(df): # Asigna de forma aleatoria horas para poder ejecutar las estrategias
    hours = random.randint(8, 23) # Genero de forma aleatoria horas
    return datetime.timedelta(days=0, hours=hours, minutes=0, seconds=0)
  

def columns_generation(df):
    df['HOUR'] = df['FECHAS'].apply(random_hours)
    df['HOUR'] = df['HOUR'].apply(lambda x: x.components.hours)
    df['DAY_MOMENT'] = df.HOUR.apply(lambda x: 'mañana' if x <= 13 else 'tarde' if x > 13 and x <= 19 else 'noche' )
    return df

def adjustments(df): # Función que incorpora una serie de ajustes (copia variable, ordena por fecha y resetea-dropea index)
    df_february_copy = df.copy()
    df_february_copy = df_february_copy.sort_values(by='FECHAS')
    df_february_copy.reset_index(inplace=True)
    df_february_copy.drop(columns={'index'},inplace=True)
    return df_february_copy


def df_to_excel_export(df,path):
    return df.to_excel(path)

# EJECUCIÓN DE FUNCIONES:

df_february = lectura_datos(r'/Users/manuelvicarioperez/VICARIO_PROJECT/STRATEGY/TEST/TEST_PAU_ECHE/3_STRATEGIES/strategies_february.csv')
df_february = columns_generation(df_february)
df_february_copy = adjustments(df_february)
df_to_excel_export(df_february_copy,r'/Users/manuelvicarioperez/VICARIO_PROJECT/STRATEGY/TEST/TEST_PAU_ECHE/3_STRATEGIES/control_strategy_febrero.xlsx')



