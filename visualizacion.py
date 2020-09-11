
#Importo las librerías necesarias para la ejecución.
#Importo mean_squared_error y mas abajo defino la función rmse porque si no me da error al importar el modelo con pickle.

import streamlit as st 
import altair as alt
import pandas as pd
import datetime
import numpy as np
import pickle
from sklearn.metrics import mean_squared_error

#Titulo de la aplicación:
st.title('ESTIMADOR DE DEMANDA DE ENERGÍA ELECTRICA EN ISLAS BALEARES')

#Inserto un comentario explicativo de como usar la aplicación:
st.markdown("""A continuación se debe seleccionar cual es el horizonte temporal sobre el que hacer la predicción
(entre 1 y 7 días). Una vez seleccionado, se debe introducir en la barra lateral la prevision de temperatura 
media para cada día:""")

def rmse(y_test, pred):
    return np.sqrt(mean_squared_error(y_test, pred))


#Defino la función que me permita definir si los días para los que se va a hacer la predición son festovos o no:
def festivos(fecha):
    if fecha in ['2020-01-01', '2020-01-06', '2020-12-25', '2020-04-09', '2020-04-10', '2020-04-13',
                 '2020-05-01', '2020-08-15', '2020-10-12', '2020-12-07', '2020-12-08', '2019-12-26']:
        return 1
    else:
        return 0
    
    
#Incorporo datos de los minutos de luz cada día para incorporar posteriormente a los datos para la predicción:
minutos = pd.read_csv('datos_finales.csv', usecols = ['fecha','minutos_luz'])
minutos = minutos[minutos['fecha'] < '2017-01-01']
minutos['mes-dia'] = minutos['fecha'].apply(lambda x: x[5:10])
minutos.drop('fecha', axis = 1, inplace = True)
minutos.drop_duplicates(inplace = True)


#Defino las fechas para las que se puede hacer predicción:
hoy = datetime.date.today()
mañana = datetime.date.today() + datetime.timedelta(days = 1)
limite = mañana + datetime.timedelta(days = 6)
rango_fechas = pd.date_range(start = mañana, end = limite, freq = 'D')

#Creo una slider para poder hacer en la App la selección del horizonte temporal sobre el que quiero hacer la predicción:
selecciona_fecha = st.slider("Seleccionar horizonte de predicción:", mañana, limite)


#Creo la variable fechas que en función del rango elegido anteriormente, cambia la frecuencia a horas:
if selecciona_fecha == mañana:
    fechas = pd.date_range(start = mañana, end = selecciona_fecha + datetime.timedelta(days = 1), freq = 'H')[:-1]
else:
    fechas = pd.date_range(start = mañana, end = selecciona_fecha + datetime.timedelta(days = 1), freq = 'H')[:-1]

    
#Creo en un sidebar las cajas para introducir la temperatura media esperada para cada uno de los días sobre los que quiero
#hacer la predicción. EL numero de cajas que aparecen en el sidebar depende del horizonte temporal elegido, es decir, si solo
#hago la predicción sobre un día, solo aparecerá una caja, pero si voy a predecir sobre la semana completa, aparecerán 7 cajas
#para que sean rellenadas (el valor por defecto de la temperatura en todas es 0):
if len(fechas)/24 == 1:
    sel_temp1 = st.sidebar.text_input('Indica temperatura día 1', value = 0)
    temp = np.repeat([sel_temp1], 24)
    
elif len(fechas)/24 == 2:
    sel_temp1 = st.sidebar.text_input('Indica temperatura día 1', value = 0)
    sel_temp2 = st.sidebar.text_input('Indica temperatura día 2', value = 0)
    temp = np.repeat([sel_temp1,sel_temp2], 24)
    
elif len(fechas)/24 == 3:
    sel_temp1 = st.sidebar.text_input('Indica temperatura día 1', value = 0)
    sel_temp2 = st.sidebar.text_input('Indica temperatura día 2', value = 0)
    sel_temp3 = st.sidebar.text_input('Indica temperatura día 3', value = 0)
    temp = np.repeat([sel_temp1,sel_temp2, sel_temp3], 24)
    
elif len(fechas)/24 == 4:
    sel_temp1 = st.sidebar.text_input('Indica temperatura día 1', value = 0)
    sel_temp2 = st.sidebar.text_input('Indica temperatura día 2', value = 0)
    sel_temp3 = st.sidebar.text_input('Indica temperatura día 3', value = 0)
    sel_temp4 = st.sidebar.text_input('Indica temperatura día 4', value = 0)
    temp = np.repeat([sel_temp1,sel_temp2, sel_temp3, sel_temp4], 24)
    
elif len(fechas)/24 == 5:
    sel_temp1 = st.sidebar.text_input('Indica temperatura día 1', value = 0)
    sel_temp2 = st.sidebar.text_input('Indica temperatura día 2', value = 0)
    sel_temp3 = st.sidebar.text_input('Indica temperatura día 3', value = 0)
    sel_temp4 = st.sidebar.text_input('Indica temperatura día 4', value = 0)
    sel_temp5 = st.sidebar.text_input('Indica temperatura día 5', value = 0)
    temp = np.repeat([sel_temp1,sel_temp2, sel_temp3, sel_temp4, sel_temp5], 24)
    
elif len(fechas)/24 == 6:
    sel_temp1 = st.sidebar.text_input('Indica temperatura día 1', value = 0)
    sel_temp2 = st.sidebar.text_input('Indica temperatura día 2', value = 0)
    sel_temp3 = st.sidebar.text_input('Indica temperatura día 3', value = 0)
    sel_temp4 = st.sidebar.text_input('Indica temperatura día 4', value = 0)
    sel_temp5 = st.sidebar.text_input('Indica temperatura día 5', value = 0)
    sel_temp6 = st.sidebar.text_input('Indica temperatura día 6', value = 0)
    temp = np.repeat([sel_temp1,sel_temp2, sel_temp3, sel_temp4, sel_temp5, sel_temp6], 24)
    
elif len(fechas)/24 == 7:
    sel_temp1 = st.sidebar.text_input('Indica temperatura día 1', value = 0)
    sel_temp2 = st.sidebar.text_input('Indica temperatura día 2', value = 0)
    sel_temp3 = st.sidebar.text_input('Indica temperatura día 3', value = 0)
    sel_temp4 = st.sidebar.text_input('Indica temperatura día 4', value = 0)
    sel_temp5 = st.sidebar.text_input('Indica temperatura día 5', value = 0)
    sel_temp6 = st.sidebar.text_input('Indica temperatura día 6', value = 0)
    sel_temp7 = st.sidebar.text_input('Indica temperatura día 7', value = 0)
    temp = np.repeat([sel_temp1,sel_temp2, sel_temp3, sel_temp4, sel_temp5, sel_temp6, sel_temp7], 24)
    
temperatura = pd.DataFrame()
temperatura['temp'] = temp
temperatura['temp'] = temperatura['temp'].apply(lambda x: float(x))


#Defino el dataframe que voy a pasar al modelo con los datos para hacer la predicción. Creo las columnas fecha (obtenida
#en función de la selección en la App) y el día de la semana que es:
X = pd.DataFrame()
X['fecha'] = fechas
X['fecha'] = pd.to_datetime(X['fecha'])
X['dia_semana'] = X['fecha'].dt.weekday_name
X = X.join(pd.get_dummies(X['dia_semana']))

#Debido a que si no hacemos la predicción sobre los 7 días no vamos a poder tener todas las dummies que necesita el modelo,
#en el caso de que no se hayan creado, las creo por fuera:
for dia in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
    if dia not in X.columns:
        X[dia] = 0

#Añado las columnas hora, minutos_luz, festivo y tmed:
X['hora'] = X['fecha'].apply(lambda x: str(x)).apply(lambda x: int(x[11:13]))
X['mes-dia'] = X['fecha'].apply(lambda x: str(x)).apply(lambda x: x[5:10])
X = X.merge(minutos, left_on = 'mes-dia', right_on = 'mes-dia')
X['festivo'] = X['fecha'].apply(lambda x: str(x)).apply(lambda x: festivos(x))
X['tmed'] = temperatura['temp']


#Hago la selección de variables en el orden que deben estár para aplicarlas al modelo de predicción:
XF = X[['tmed', 'minutos_luz', 'festivo', 'hora', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]


#Cargo el modelo ya entrenado (fuen entrenado en el notebook modelos):
modelo = pickle.load(open('modelo_pred.pkl', 'rb'))


#Hago la prediccicón con los datos vinculados a las fechas seleccionadas a través de la App:
prediccion = pd.DataFrame()
prediccion['fecha'] = X['fecha']
prediccion['prediccion'] = modelo.predict(XF)
prediccion = prediccion.join(X[['dia_semana','tmed', 'minutos_luz', 'festivo', 'hora']], on = prediccion.index)


#Represento gráficamente el resultado de la predicción:
grafico = alt.Chart(prediccion).mark_bar().encode(
    x = alt.X('fecha', axis=alt.Axis(title='Fecha')),
    y = alt.Y('prediccion', axis=alt.Axis(title='Energía Eléctrica (MW/h)')),
    color = alt.Color('prediccion', legend=alt.Legend(title="MW/h"), scale=alt.Scale(scheme='lightmulti')),
    tooltip = 'prediccion'
).properties(
    title = 'Predicción de la demanda de energía eléctrica',
    width = 800,
    height = 500)

#Hago una agrupación en función del día de la semana que me calcule cual ha sodo la demanda de energía eléctrica media
#por hora cada dia y posteriormente lo represento en un gráfico:
agrup1 = prediccion.groupby(by = 'dia_semana').mean()
agrup1['Dia'] = agrup1.index


grafico2 = alt.Chart(agrup1).mark_bar(size = 20).encode(
    x = alt.X('Dia', axis=alt.Axis(title='Fecha')),
    y = alt.Y('prediccion', axis=alt.Axis(title='Energía Eléctrica')),
    color = alt.Color('prediccion', legend=alt.Legend(title="MW/h"), scale=alt.Scale(scheme='lightmulti')),
    tooltip = 'prediccion'
).properties(
    title = 'Demanda de energía media por hora cada día',
    width = 800,
    height = 500)

#Hago una agrupación en función del día de la semana que me calcule cual ha sido la demanda de energía eléctrica a lo largo
#de todo el día (la suma de todas las horas de cada día) y lo represento en otro gráfico:
agrup2 = prediccion.groupby(by = 'dia_semana').sum()
agrup2['Dia'] = agrup2.index

grafico3 = alt.Chart(agrup2).mark_bar(size = 20).encode(
    x = alt.X('Dia', axis=alt.Axis(title='Fecha')),
    y = alt.Y('prediccion', axis=alt.Axis(title='Energía Eléctrica')),
    color = alt.Color('prediccion', legend=alt.Legend(title="MW"), scale=alt.Scale(scheme='lightmulti')),
    tooltip = 'prediccion'
).properties(
    title = 'Demanda de energía total por día',
    width = 800,
    height = 500)

st.write(grafico)
st.write(grafico2)
st.write(grafico3)
st.write(prediccion)
