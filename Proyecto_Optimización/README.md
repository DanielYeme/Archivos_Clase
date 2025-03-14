#Tech Giants Stock Market Analysis (2020-2023)

##Resumen del proyecto.
<p>
Este proyecto analiza el rendimiento del mercado de valores de siete gigantes tecnológicos: Google (GOOGL), Meta (META), Microsoft (MSFT), Apple (AAPL), Tesla (TSLA), Amazon (AMZN) y Oracle (ORCL), utilizando datos históricos desde enero de 2020 hasta diciembre de 2023.
</p>
##Objetivo principal
El análisis de este proyecto se centra en observar las tendencias clave, volatilidad y retorno acumulado de las empresas con mejor desempeño y brindar recomendaciones para inversionistas y stakeholders.

###Metodología y Codigo explicado
1. Primero se busco en la pagina de Kaggle un archivo csv para poder realizar un analisis de sus datos. En nuestro caso elegimos el dataset proporcionado por Tech Giants. 
Link: https://www.kaggle.com/code/jeleeladekunlefijabi/tech-giants-stock-data-eda-analysis

2. Una vez descargado el archivo CSV, se guardo el archivo en la misma carpeta que el proyecto para posteriormente comenzar a editar el Jupyter Notebook.

3. Se aseguró que todas las librerias estuvieran instaladas en Visual studio utilizando el comando pip install como se muestra a continuacion:
```
pip install pandas
pip install numpy
pip install matplotlib.pyplot
pip install seaborne
```
4. Para empezar el codigo primero se realizó una sección que sirviera para leer todos nuestros datos del archivo CSV adecuadamente

```
import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv("Tech Giants Stock Market Data (Processed).csv")

# Mostrar las primeras 10 filas
df.head(10)
```
> Sección del codigo utilizada para leer el archivo CSV en un dataframe utilizando la libreria de pandas.

```
# Mostrar información sobre el DataFrame
df.info()

# Mostrar estadísticas descriptivas del DataFrame
df.describe()
```
>Sección para poder ver de mejor manera la información de nuestro dataframe.

5.Filtrado de Datos

- En base a los datos obtenidos previamente con el codigo df.info se eliminaron las filas que contenian valores 0 en las columnas pct_change, moving_avg_7D y moving_avg_30D.

- Se usa .loc[] para seleccionar solo las filas que cumplen con la condición.

- Ademas tambien se uso axis=1 para indicar que la evaluación se hace por fila.

- Mientras que all se utiliza para verificar si todas las condiciones en la fila son verdaderas (en caso de querer verificar si al menos una es verdadera, se podría usar any).

```
AccionesTecnologicas_cleaned = df.loc[
    (df[['pct_change', 'moving_avg_7D', 'moving_avg_30D']] != 0).all(axis=1)
]

# axis=1 indica que la evaluación se debe hacer por fila. Y el all, para evaluar que todas las condiciones se cumplanm
(df[['pct_change', 'moving_avg_7D', 'moving_avg_30D']] != 0).all(axis=1)

# Reemplazar los valores de 0 con el promedio en pct_change
# Visualizar el promedio
pct_change_promedio = AccionesTecnologicas_cleaned['pct_change'].mean()
pct_change_promedio

# reemplazar los indices de pct_change que tienen valor 0 por el promedio de la columna
AccionesTecnologicas_cleaned.loc[AccionesTecnologicas_cleaned['pct_change'] == 0, 'pct_change'] = pct_change_promedio

# Reemplazar los valores de 0 con el promedio en moving_avg_7D
# Visualizar el promedio
moving_avg_7D_promedio = AccionesTecnologicas_cleaned['moving_avg_7D'].mean()
moving_avg_7D_promedio

# reemplazar los indices de moving_avg_7D que tienen valor 0 por el promedio de la columna
AccionesTecnologicas_cleaned.loc[AccionesTecnologicas_cleaned['moving_avg_7D'] == 0, 'pct_change'] = moving_avg_7D_promedio

# Reemplazar los valores de 0 con el promedio en moving_avg_30D
# Visualizar el promedio
moving_avg_30D_promedio = AccionesTecnologicas_cleaned['moving_avg_30D'].mean()
moving_avg_30D_promedio

# reemplazar los indices de moving_avg_30D que tienen valor 0 por el promedio de la columna
AccionesTecnologicas_cleaned.loc[AccionesTecnologicas_cleaned['moving_avg_30D'] == 0, 'pct_change'] = moving_avg_30D_promedio

# Visualizar los indices de SkinThickness que tienen valor 0
AccionesTecnologicas_cleaned.loc[AccionesTecnologicas_cleaned['moving_avg_30D'] == 0, 'moving_avg_30D'].head(20)
```
>Sección del código para limpiar el DataFrame eliminando filas con valores 0 en las columnas de interés y borrar outliners.

6. Estadistica Descriptiva

El siguiente script realiza diversos operaciones estadísticas para el análisis de los precios ajustados de un activo financiero, asi como las tasas de rendimiento (cambio porcentual).


El código realiza los siguientes cálculos utilizando la librería `numpy` de Python:

 **Precio Ajustado:**
   - El precio ajustado (representado por la columna `Adj Close`) es el valor del activo ajustado por eventos corporativos como dividendos y splits. Este cálculo ayuda a obtener una visión más precisa del rendimiento de la inversión.
     
   - Se calculan las siguientes estadísticas sobre la columna `Adj Close`:
     - **Media**: Promedio de todos los precios ajustados.
     - **Mediana**: El valor central de los precios ajustados (cuando están ordenados).
     - **Desviación Estándar**: Mide la dispersión de los precios ajustados con respecto a la media.

 **Tasa de Rendimiento (Cambio Porcentual):**
   - La tasa de rendimiento se calcula como el cambio porcentual diario entre los precios ajustados de un día y el día anterior.
     
   - Las siguientes estadísticas se calculan sobre la columna de cambio porcentual (`pct_change`):
     - **Media**: Promedio del cambio porcentual diario.
     - **Desviación Estándar**: Mide la variabilidad de las tasas de rendimiento a lo largo del tiempo.

## Cálculos Realizados

- **Media del Precio Ajustado**: La media aritmética de todos los valores en la columna `Adj Close`.
- **Mediana del Precio Ajustado**: El valor central en la distribución de precios ajustados.
- **Desviación Estándar del Precio Ajustado**: La dispersión o variabilidad de los precios ajustados con respecto a la media.
- **Media de la Tasa de Rendimiento**: El promedio de todos los cambios porcentuales diarios calculados a partir de los precios ajustados.
- **Desviación Estándar de la Tasa de Rendimiento**: La dispersión de las tasas de rendimiento a lo largo del tiempo.

## Código

```
import numpy as np

# Calcular la columna de cambio porcentual
df['pct_change'] = df['Adj Close'].pct_change()

# Calcular la media y mediana del precio ajustado
media_adj_close = np.mean(df['Adj Close'])
mediana_adj_close = np.median(df['Adj Close'])

print(f"Media de Precio Ajustado: {media_adj_close}")
print(f"Mediana de Precio Ajustado: {mediana_adj_close}")

# Calcular la desviación estándar del precio ajustado
std_adj_close = np.std(df['Adj Close'])
print(f"Desviación Estándar del Precio Ajustado: {std_adj_close}")

# Calcular la media del cambio porcentual (Tasa de rendimiento)
media_pct_change = np.mean(df['pct_change'])

# Calcular la desviación estándar de la Tasa de Rendimiento
std_pct_change = np.std(df['pct_change'])

print(f"Desviación Estándar de la Tasa de Rendimiento: {std_pct_change}")
print(f"Media de Tasa de rendimiento: {media_pct_change}")
```

7. Análisis Gráfico de Acciones Tecnológicas

Este script utiliza las bibliotecas `matplotlib` y `seaborn` para visualizar diferentes aspectos de un conjunto de datos sobre acciones tecnológicas. Las visualizaciones incluyen gráficos de barras, histogramas, boxplots y gráficos de dispersión, que permiten analizar las distribuciones de los precios ajustados, volúmenes de transacciones y tasas de rendimiento de estas acciones.


### 1. Gráfico de Barras de Precios Ajustados por Acción

-Este gráfico de barras muestra los precios ajustados (`Adj Close`) de cada acción tecnológica en el conjunto de datos. El eje `x` contiene los símbolos de las acciones (`Ticker`), y el eje `y` muestra el precio ajustado de cierre de cada acción.

-Nos sirve para identificar aquellos precios de lacciones más altos o bajos con respecto a los otros activos, en cierto momento.

```
plt.figure(figsize=(6,4))
plt.bar(AccionesTecnologicas_cleaned['Ticker'], AccionesTecnologicas_cleaned['Adj Close'])
plt.xlabel('Acciones Tecnologicas')
plt.ylabel('Cierres Ajustados')
plt.title('Distribución de Cierres por Acción')
plt.show()
```

### 2. Histograma de Precios de Cierre Ajustados

- Este gráfico nos muestra la distribucción de precios ajustados de todas las acciones tecnologicas. Se incluye una curva de densidad (kde) que permite observar la forma de la distribución.

- Es bastante util para encontrar aquellas distribucciones sesgadas, normales o cualquier anomalia en los precios.

```
plt.figure(figsize=(10, 5))
sns.histplot(AccionesTecnologicas_cleaned['Adj Close'], bins=50, kde=True)
plt.title("Distribución de Precios de Cierre Ajustados")
plt.xlabel("Precio de Cierre Ajustado")
plt.ylabel("Frecuencia")
plt.show()
```

### 3. Gráfico de Barras de Volumen de Transacciones por Acción

- Este tipo de gráfico de barras fue seleccionado para observar el volumen de transacciones (Volume) para cada acción. En el eje (x) tenemos los Tickers, mientras que en el eje (y) nos muestra su volumen.
  
- Es especialmente importante para identificar aquellas acciones con un mayor volumen, lo que significa su facilidad para relizar transacciones de compra y venta.

```
plt.figure(figsize=(6,4))
plt.bar(AccionesTecnologicas_cleaned['Ticker'], AccionesTecnologicas_cleaned['Volume'])
plt.xlabel('Acciones Tecnologicas')
plt.ylabel('Cierres Ajustados')
plt.title('Distribución de Cierres por Acción')
plt.show()
```

### 4. Histograma de Tasas de Rendimiento (Cambio Porcentual)

- El objetivo del siguiente histograma es mostrar la  distribucion de las tasas de rendimiento, sinedo aquellos cambios porcentuales entre los precios ajustados en diferentes días. Es fundamental apreciar como se representa una curva de densidad para relacionar la forma de su distribucción.

- Esta gráfica nos permite sbaer la volatilidad existente en cada una de los activos. Ademas de comprender cual es su rendimiento diario y su riesgo asociado.

```
plt.figure(figsize=(10, 5))
sns.histplot(AccionesTecnologicas_cleaned['pct_change'], bins=50, kde=True)
plt.title("Distribución de Tasa de Rendimiento")
plt.xlabel("Tasa de Rendimiento")
plt.ylabel("Frecuencia")
plt.show()
```
### 5. Boxplot de Precios Ajustados por Empresa

- Los gráficos Boxplots nos ayudan a visualizar cuartiles, mediana y posibles valores atipicos en nuestra información del dataset.

- Es de gran ayuda al momento de comparar la dispersión y la mediana de precios ajustados entre distintas empresas tecnologicas.

```
plt.figure(figsize=(12, 6))
sns.boxplot(x="Ticker", y="Adj Close", data=AccionesTecnologicas_cleaned)
plt.title("Distribución de Precios de Cierre Ajustados por Empresa")
plt.xlabel("Empresa")
plt.ylabel("Precio de Cierre Ajustado")
plt.show()
```

### 6. Histograma de Volumen de Transacciones

- Este histograma nos permite comprender la variabilidad de los volumenes de transacción a lo largo del tiempo de todas las acciones tecnologicas.

- Nos indica aquellos periodos de alta o baja actividad en el mercado.

```
sns.histplot(AccionesTecnologicas_cleaned['Volume'], bins=50, kde=True)
plt.title("Distribución de Volumen")
plt.xlabel("Volumen")
plt.ylabel("Frecuencia")
plt.show()
```

### 7. Gráfico de Dispersión entre Volumen y Precio de Cierre Ajustado

- Se trata de un grafico de dispersión que muestra la relación entre el volumen y los precies de cierre de manera ajustada. Cada punto de diferente color corresponde a una compañia.

- Nos llega a ser de gran utilidad al momento de construir las correlaciones de los activos.
  
```
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Volume", y="Adj Close", hue="Ticker", data=AccionesTecnologicas_cleaned, alpha=0.6)
plt.title("Relación entre Volumen de Transacciones y Precio de Cierre Ajustado")
plt.xlabel("Volumen de Transacciones")
plt.ylabel("Precio de Cierre Ajustado")
plt.legend(title="Empresa")
plt.show()
```
8 . Finalmente, para encontrar una correlacion entre las empresas, utilizamos un mapa de calor implementado con un seaborn para justamente encontrar dichas similitudes.

```
import seaborn as sns

# Al tener un dataframe con un formato revuelto, utilizamos pivot para reorganizarlo antes de calcular la correlación de los activos
# de acuerdo a su valor de cierre

df_pivot = df.pivot(index='Date', columns='Ticker', values='Close')

# Calcular la correlación entre los precios de cierre
correlacion = df_pivot.corr()


# Crear el mapa de calor
plt.figure(figsize=(10,6))
sns.heatmap(correlacion, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Mapa de Calor de la Matriz de Correlación')
plt.show()
```
>Fragmento de codigo dedicado a crear un mapa de calor.

<p>
Con esta correlación podemos construir un portafolio de inversión destinado a empresas tecnologicas que permitan una mejor diversificación al presentar una menor correlación, lo que minimiza nuestro riesgo y al mismo tiempo podemos maximar las ganancias o rentabilidad con una buena optimización en la elección de activos y su respectivo peso.
</p>
