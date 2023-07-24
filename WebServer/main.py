import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app= FastAPI()

@app.get('/')#sintaxis, decorador. Cual es la ruta x ingresar x la web
def getList(): 
    return [1,2,3,] #devuelve una lista

@app.get('/contact') #sintaxis, decorador. Cual es la ruta x ingresar x la web
def getList():
    return { 'name': 'Platzi' }

@app.get("/pagina", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Un titulo emocionante</title>
        </head>
        <body>
            <h1>Un cuerpo genial!</h1>
            <h2>Soy una figura ❤ </h2>
        </body>
    </html>
    """

def run():
    store.getCategories()

if __name__=='__main__':
    run()

    