import matplotlib.pyplot as plt

#definimos la funcion para generar el pie
def  generate_pie_chart():
    labels =['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots() #obtenemos la figura, coordenadas desde matplotlib
    ax.pie(values, labels= labels) #queremos generar el pie, enviare los valores
    plt.savefig('pie.png') #Guardame la imagen en un archivo
    plt.close()