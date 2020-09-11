# PREDICCIÓN DE LA DEMANDA DE ENERGÍA ELÉCTRICA EN ISLAS BALEARES
### TFM MASTER DATA SCIENCE Kschool ED.19 - Pablo Hernanz Boiza

## 1 - Introdución y Motivación del trabajo:
El objetivo de éste trabajo es crear una App que permita hacer predicciones sobre la demanda de energía eléctrica en Islas Baleares con un horizonte de predicción máximo de una semana. Es decir, te permitirá hacer predicción con frecuencia horaria desde el día siguiente al actual, hasta un máximo de siete días.  
  
La utilidad de crear una App como ésta se basa en la importancia que puede tener para las eléctricas conocer la cantidad de energía demandada a cada hora en una determinada región. Si se tiene una idea de cual va a ser esa demanda, se puede ajustar la producción de energía e incluso se podría determinar si esa demanda se podría cubrir utilizando fuentes de energía alternativas.  

## 2 - Esquema del repositorio del TFM en GitHub:
- Datos_sin_tratar: Carpeta que contiene los archivos con los datos de partida. Los archivos que van a ser utilizados de ésta carpeta se detallan en el apartado "Descripción de los datos de partida".
- exploración_datos.ipynb: Primer notebook a ejecutar.
- modelos.ipynb: Segundo notebook que se debe ejecutar.
- visualizacion.ipynb: Ultimo notebook a ejecutar.
- datos_finales.csv: Archivo csv que se genera después de la ejecución del notebook exploracion_datos.ipynb.
- modelo_pred.pkl: Modelo entrenado que se guarda al ejecutar el notebook modelos.ipynb.
- modelo_inf_pkl: Modelo entrenado que se guarda al ejecutar el notebook modelos.ipynb, (pero finalmente no usado).
- modelo_sup_pkl: Modelo entrenado que se guarda al ejecutar el notebook modelos.ipynb, (pero finalmente no usado).
- visualizacion.py: Archivo python que se crea al ejecutar la primera celda del notebook visualizacion.ipynb.
  
## 3 - Descripción de los datos de partida:
Para la realización del trabajo, se ha partido de los datos contenidos en los siguientes archivos:  
- demanda_baleares_16-19.csv: Que contiene los datos de la demanda de energía eléctrica (MW/h) en las Islas Baleares entre el año 2016 y el año 2019 con frecuencia horaria. Por lo que nos salen 35064 filas.
- meteo_mallorca.txt: Que contiene información sobre la temperatura diaria de Palma de Mallorca entre el año 2016 y 2019.
- horas_sol-2020.txt: En el que encontramos, en forma de tabla (días en filas y meses en columnas, las horas de salida y puesta de sol para todo el año 2020. Aunque entre los distintos años hay alguna pequeña diferencia en las horas de salida y puesta de sol para un mismo día, por la poca diferencia y para simplificar se utilizan esos datos de forma común para todos los años.

## 4 - Descripción de los notebooks realizados:
A continuación se describen de forma resumida los notebooks realizados puesto que, en los propios notebooks, se encuentran detallados los pasos realizados en cada uno de ellos:
- exploracion_datos.ipynb: En éste notebook se limpian y transforman los datos contenidos en los archivos mencionados en el punto anterior. A partir de éstos datos se crean nuevas variables, obteniendo un dataframe que será el utilizado en los siguientes notebooks en la predicción de modelos o para la visualización. Este dataframe final se guarda en formato csv, generandose así el archivo datos_finales.csv.
- modelos.ipynb: En éste notebook se alimenta del archivo resultante del notebook exploracion_datos.ipynb, es decir, el archivo datos_finales.csv. En éste notebook se estudian de nuevo los datos para determinar cuales van a ser utilizadas en los modelos de predicción. Una vez hecho ésto, se genran los datos de entrenamiento y de test y se plantean diferentes modelos y se comparan para ver cual nos da mejores predicciones. Tras ésto, se guarda el modelo elegido ya entrenado para que pueda ser utilizado a posteriori con nuevas prediccciones que se quieran hacer. El modelo queda guardado con el nombre modelo_pred.pkl.
- visualizacion.ipynb: En éste último notebook se desarrolla el código para la creación de la App con Streamlit, de forma que se consige una visualización interactiva de los resultados. Éste notebook está compuesto de sólo dos celdas; la primera en la que está escrita todo el código de la App y que ademas genera el archivo visualizacion.py, y la segunda que sirve para ejecutar la App (se generan los enlaces para copiar en el navegador).

## 5 - Ejecución del proyecto y librerias necesarias:
### 5.1 - Librerias necesarias:  
Para la correcta ejecución del proyecto se debe tener instalado:  

numpy | pandas | matplotlib | datetime | seaborn | sklearn | pickle | streamlit | altair

### 5.2 - Ejecución del proyecto:
En principio el orden de ejecución de los notebooks es el siguiente:
- En primer lugar se debe ejecutar el notebook exploracion_modelos.ipynb. Después de la ejecución se genera el archivo datos_finales.csv que es empleado en el siguiente notebook.
- El segundo notebook a ejecutar es modelos.ipynb. En éste notebook se utiliza el archivo datos_finales.csv y tras su ejecución se guarda el modelo de predicción entrenado (modelo_pred.pkl).
- Por último, se debe ejecutar el notebook visualizacion.ipynb. Este notebook crea el archivo python visualizaciones.py y permite ejecutar la App mediante la instrucción: !streamlit run visualizacion.py, desde linux.

Por otro lado, en el repositorio ya están guardados todos los archivos que se generan al ejecutar los notebooks, por lo que solo sería necesario ejecutar el notebook visualizacion.ipynb y copiar en el navegador la url que abrira la App. O simplemente desde la consola de linux, y dentro del directorio del TFM, ejecutar "streamlit run visualiacion.py" y copiar la url que salga en el navegador.

## 6 - Funcionamiento de la App:
La App funciona de la siguiente forma:
- En primer lugar hay que seleccionar mediante la slider el horizonte temporal sobre el que queremos hacer la predicicón. Puede ser desde un día (valor por defecto) a una semana completa. La primera fecha sobre la que se puede hacer predicción es el día siguiente al que nos encontremos cuando estemos utilizando la App.
- En segundo lugar, al seleccionar el rango de fechas sobre el que queremos hacer la predicción, nos aparecen en la sidebar tantas cajas de texto como días queramos predecir. En éstas cajas se debe introducir la temperatura media que se espera para dichos días.
