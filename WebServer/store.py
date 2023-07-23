import requests #Importamos la libreria requests

def getCategories(): #funcion
#hacia donde hacer la solicitud (solicitud a API)
    r = requests.get('https://api.escuelajs.co/api/v1/categories') 
    print(r.status_code) #podemos obtener el estado del API
    print(r.text)#Recibe una lista
    print(type(r.text))#El tipo de doc es un string
    categories = r.json()#lo tranf auto en lista,dicc
    for category in categories:
        print(category['name'])

'''
Aprendizajes:
coloque categories['name'] pero no puede obtener ese atributo de la lista completa

'''
