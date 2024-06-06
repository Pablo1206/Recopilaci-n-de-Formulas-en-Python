#Instalar Librerias e importar
pip install numpy



### Definir listas ###
x = ["a","b","c","d"]
print(x[0]) # Seleccioonar el primer valor
print(x[1:3]) # Seleccionar el segundo valor y el tercero B y C
print(x[1:]) # Seleccionar el segundo valor en adelante
print(x[:3]) # Seleccionar del primero hasta el tercero

### Operaciones con Listas ###
x = [1,2,3,4]
y = [1,2,3,4]
print(x + y) # Unir las dos listas
print(x * 2) # Duplica la lista 

### Operaciones con Listas ###
diccionario ={"PH SV": 1,
              "WD SV": 4,
              "CW SV": [40, 50, 60]
             }
print(diccionario.keys()) # Obtiene la llave de los diccionarios
print(diccionario.values()) # Obtiene los valores de cada diccionario
print(diccionario["CW SV"]) #Obtengo el valor de la llave que referencio 
print(diccionario["CW SV"][1]) #Obtengo el segundo valor de la lista de mi llave 

### Operaciones con NumPY
import numpy as np
lista = [50,60,70,80,90]
np.mean(lista) # devuelve el promedio de los valores de la lista
np.sum(lista) # devuelve la suma de los valores de la lista
np.max(lista) # devuelve el max
np.min(lista)  # devuelve el min

### Uso de Bucles ###
#ejemplo con listas
lista = ["PH SV", "WD SV", "KFC SV","WD SV"]
Venta = 50
for marca in lista: 
    print(fr"La venta de {marca} es de {Venta}")
    Venta = Venta + 50
    
#ejemplo con diccionarios
diccionario = {"PH SV": ["Javier","30",200],
              "WD SV": ["Alex","30",100],
              "CW SV": ["Jason","20",90]
             }
incremento = 2
venta_acumulada = 0 
for marca,valores in diccionario.items(): 
    print(fr"El analista de BI de {marca} es {valores[0]} y tiene {valores[1]} años")
    venta_x2 = valores[2] + incremento
    print(fr"la venta de la marca fue de {valores[2]} y su incremento fue de {venta_x2} ")
    venta_acumulada = venta_acumulada + valores[2]
print(fr"la venta acumulada de PRA fue de {venta_acumulada}")

#Ejemplo con dos bucles
lista = [2024,2023,2022]
diccionario = {"PH SV": [2000,2100,2500],
              "WD SV": [1500,1200,1000],
              "CW SV": [1000,999,995]
             }
x = 0
for marca,valores in diccionario.items():
    for  anio in lista: 
        venta = np.random.randint(900,3000)
        PPTO = valores[int(x)]
        print(fr"la venta de {marca} en el año {anio} fue de {venta} y su PPTO era de {PPTO}")
        x = x + 1
    x = 0

### Pandas ###
import pandas as pd

data = {
    'Nombre': ['León', 'Tigre', 'Jirafa', 'Elefante', 'Cebra', 'Leopardo', 'Hipopótamo', 'Rinoceronte'],
    'Clase': ['Mamífero', 'Mamífero', 'Mamífero', 'Mamífero', 'Mamífero', 'Mamífero', 'Mamífero', 'Mamífero'],
    'Orden': ['Carnívoro', 'Carnívoro', 'Herbívoro', 'Herbívoro', 'Herbívoro', 'Carnívoro', 'Herbívoro', 'Herbívoro'],
    'Hábitat': ['Savannah', 'Selva', 'Savannah', 'Selva', 'Savannah', 'Selva', 'Agua dulce', 'Savannah'],
    'Peso (kg)': [190, 250, 1200, 5000, 300, 60, 1500, 2300],
    'Longitud (m)': [2, 2.5, 5.5, 6, 2.2, 1.5, 3.5, 4]
}

df = pd.DataFrame(data) # Crear Dataframe con la información
print(df.columns) #Obtener nombre de las columnas del df
print(df.head()) #Obtener las primeras 5 filas del df
print(df.columns) #Obtener nombre de las columnas del df
print(df.values) #Obtener los valores del df
print(df.index) #obtener el no de filas 

print(df["Nombre"]) #Obtener solo una columna 
print(df[["Nombre",'Peso (kg)']]) #Obtener dos columnas o más 
print(df[df['Peso (kg)']>1000]) #Obtener el df con condicionales
print(df[(df['Peso (kg)']>2000) & (df['Hábitat']=='Savannah')]) #Obtener el df con condicionales de AND
print(df[(df['Orden']>'Carnívoro') | (df['Hábitat']=='Savannah')]) #Obtener el df con condicionales de OR
print(df[(df['Orden']>'Carnívoro') | (df['Hábitat']=='Savannah')]) #Obtener el df con condicionales de OR
df["Peso (lb)"] = df['Peso (kg)']*2.2  #crear una nueva columna
df_peso = df[df["Peso (lb)"]== 700] #crear un df condicionado
df = df.sort_values("Peso (lb)", ascending = False) # Ordenar el df de forma descendente
print(df["Peso (lb)"].max()) #Obtener el peso maximo

## botar columnas
df = df.drop("Peso (lb)",axis =1)

## función personalizada ##
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
print(df["Peso (lb)"].agg(iqr))

## Funciones de tiempo ##
temperatures["year"] = temperatures["date"].dt.year

## Funciones .cumsum()  (Acumulado) y .cummax() (mayor valor en el df) ##

## Fución .drop_duplicates(subset = ["store","department"]) o vacio para aplicarlo a todo al df ##
Nduplicados = df.drop_duplicates()


## value counts ## 
conteo_clase = df['Clase'].value_counts()
print(conteo_clase)
# Obtén la proporción de tiendas de cada type
proporcion_clase  = df['Clase'].value_counts(normalize =True)
print(proporcion_clase)
# Cuenta el número de cada department y ordena puede ocuparse tambien la propocion
clase_ord = df['Clase'].value_counts(sort = True)
print(clase_ord)

## groupby ##
df_agrupado = df.groupby("Nombre")['Peso (kg)'].mean()
df_agrupado = df.groupby("Nombre")['Peso (kg)'].agg([np.min,np.max,np.mean])

## pivot_table ##
# aggfunc por defecto es Mean() , fill_value, margins, margins_name, sort
df_agrupado = df.pivot_table(index='Orden', columns='Hábitat', values= 'Longitud (m)', aggfunc='count',margins = all, fill_value=0)

## Indices ##
df_index = df.set_index('Orden') # definir indice
df_index = df.reset_index(drop =False )  #Quitar indice , drop determina si se borra la varaible o no

# filtrar filas por valor de indice por .loc()
lugar = ['Savannah']
df_index = df.set_index('Hábitat') # definir indice
df_index.loc[lugar]

#doble indice
df_index = df.set_index(['Hábitat', 'Orden']) # definir doble indice
filtro = [('Savannah','Carnívoro'), ('Savannah','Herbívoro')]
df_index.loc[filtro]

#Ordenar el indice 
df_index.sort_index(level=['Hábitat', 'Orden'], ascending=[True, False])

#Cortar dataframe por indices y columnas 
df_index = df.set_index(['Hábitat', 'Orden'])
df_index = df_index.sort_index()
df_index.loc[('Savannah','Herbívoro'):('Selva','Herbívoro'),'Nombre':'Peso (kg)']

#trabajar con fechas también es facil con index, ya que puedes filtrar por parte de la fecha .loc["2010-08":"2011-02"]
#Siempre es necesario usar .sort_index()

## Crear columnas condicionales ##
# Método .loc (no tan recomendado)
df.loc[df['Peso (kg)']>=1000, "Categoría Peso"] = "Pesado"
df.loc[(df['Peso (kg)']<1000) & (df['Peso (kg)']>400) , "Categoría Peso"] = "Mediano"
df.loc[df['Peso (kg)']<= 400, "Categoría Peso"] = "Ligero"

#Método con NumPy (díficil de leer)
cond = [
    (df['Peso (kg)']>= 1000),
    (df['Peso (kg)']<1000) & (df['Peso (kg)']>400),
    (df['Peso (kg)']<= 400)
]
val = ["Pesado","Mediano","Ligero"]
df["Categoría Peso"] = np.select(cond,val)

# Map y apply 
def categorizar_peso(peso):
    if peso >= 1000:
        return "Pesado"
    elif 400 < peso < 1000:
        return "Mediano"
    else:
        return "Ligero"
df['Categoría Peso'] = df['Peso (kg)'].map(categorizar_peso).fillna("-")
df['Categoría Peso'] = df['Peso (kg)'].apply(categorizar_peso).fillna("-")

# Columna Condicionada
df['Categoría Peso'] =  ["Pesado" if i >= 1000 else "Mediano" if i < 1000 and i > 400 else "Ligero" for i in df['Peso (kg)']  ]


## Concat y Merge ##
df = df.merge(equivalencia, on = ["col1","col2"], how= left)
df_consolidado = pd.concat([df_consolidado , df], ignore_index = True)

## Modificar el Nombre de una columna ## 
#Modificar una columna
df.rename(columns={'Nombre': 'Especie'}, inplace=True)

#Modificar todas las columnas
nuevos_nombres = ['Habitat', 'Order', 'Species', 'Weight (kg)']
df.columns = nuevos_nombres

## Modificar el orden del df ##
#manual 
nuevo_orden = ['Nombre', 'Hábitat', 'Orden', 'Peso (kg)']
df = df[nuevo_orden]

#Elegir la primera columna
nuevo_orden = [columna_principio] + [col for col in df.columns if col != columna_principio]
df = df[nuevo_orden]

# Definir las ultimas columnas
nuevo_orden = [col for col in df.columns if col != columna_final] + [columna_final]
df = df[nuevo_orden]