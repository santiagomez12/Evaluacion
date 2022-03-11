import pandas as pd
df = pd.read_csv('evaluacion.csv', sep=';')

df.head()
df.info()
#1

def valor_promedio(municipio):
  try:
    df["area_precio"] = df["precio"] / df["area"]
    return round(df["area_precio"].where((df["municipio"].str.lower())==municipio.lower()).dropna().mean(),2)
  except:
    print("No se encuentra en la base de datos")
  
valor_promedio("medellin")

#2

def lista_precios(municipio, tipo):
  try:
    df_filtro=df.where((df["municipio"].str.lower())==municipio.lower()).dropna()
    df_filtro=df_filtro.where((df["tipo"].str.lower())==tipo.lower()).dropna()  
    return df_filtro["precio"].astype(int).sort_values(ascending=False).tolist()
  except:
    print("no se encuentra en la base de datos")
  

lista_precios("medellin","apartamento")

#3

def lista_precios_umbral(municipio, tipo, umbral):
  
  try:
    df_filtro=df.where((df["municipio"].str.lower())==municipio.lower()).dropna()
    df_filtro=df_filtro.where((df["tipo"].str.lower())==tipo.lower()).dropna() 
    df_filtro=df_filtro.where(df["precio"]>=umbral).dropna()
    return df_filtro["precio"].astype(int).sort_values(ascending=False).tolist()
  except:
    print("no se encuentra en la base de datos")


lista_precios_umbral("medellin","apartamento",200)

#4

def promedio_area():
  return df["area"].mean()

promedio_area()

#5

def lista_municipios():
  return df["municipio"].unique().tolist()

lista_municipios()

#6

def lista_areas(tipo):
  try:
    filtro = df.where((df["tipo"].str.lower())==tipo.lower()).dropna()
    lista = filtro["area"].astype(int).sort_values().tolist()
    return tuple(lista)
  except:
    print("No se encuentra en la base de datos")

lista_areas("apartamento")

#7


def ver_predio(codigo_predio):
  try:
    filtro = df.where(df["codigo_predio"]==codigo_predio).dropna()
    diccionario = {
        "codigo_predio": filtro.iloc[:,0].values[0],
        "area": filtro.iloc[:,1].values[0],
        "municipio":filtro.iloc[:,2].values[0],
        "precio":filtro.iloc[:,3].values[0],
        "tipo":filtro.iloc[:,4].values[0],
    }  
    return diccionario
  except:
    print("No se encuentra en la base de datos")


ver_predio(5)