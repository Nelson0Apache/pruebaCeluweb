import requests
from lxml import html
import json 

#Encabezado para no ser detectado 
header = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

#Url semilla 
url = 'https://www.drogueriascafam.com.co/tiendas'

#Atributo requests  peticion que se hace
repuesta = requests.get(url, headers=header)

#Arbol donde se va a generar nuesto codigo html
arbol = html.fromstring(repuesta.text)


#Contenedor donde esta todos los nombres de las droguerias 
droguerias = arbol.xpath('//*[@id="content-wrapper"]')


#Ciclo for para iterar cada una deladroguerias 
#Se obtiene el nombre, ciudad, direccion
for drogueria in droguerias:
    ciudades = drogueria.xpath('.//address/text()[4]')
    nombres = drogueria.xpath('.//h3/text()')
    direcciones = drogueria.xpath('.//address/text()[1]') 

#Aca se va a genererar un diccionario con el ciclo for  
informacion = []
#Ciclo for para iterar cada una de las droguerias 
for i in range(len(ciudades)):
    informacion.append({ ciudades[i] :  {'nombres': nombres[i], 'direcciones': direcciones[i]}})


with open('droguerias_cafam.json', mode='w', encoding='utf-8') as file:
    json.dump(informacion, file, indent=4, ensure_ascii=False)