from tkinter import *

import matplotlib.pyplot as plt


contador=1
def ecuacion(terminos, Pmuestreo,terminos2):
    global contador

    u=""
    aux=0
    u2=""
    aux2=0
    for x in terminos:
        if(x != 0):
            u2+= f"{str(terminos[aux2])}X (k- {str(round(aux,2))} ) + " 
        u+= f"{str(terminos[aux2])}X (k- {str(round(aux,2))} ) + " 
        aux+=Pmuestreo
        aux2+=1
    cadena =f"secuencia #{contador}\n{u[:-2]}"
    if(u2 != ""):
        cadena+= f"\n{u2[:-2]}"
    contador+=1
    return cadena
    
def graficar(termino,pmeustreo):
    # Datos de la señal discreta (ejemplo)
    y = pmeustreo
    #aux=0
    #for count in range(len(termino)-1):
         #aux+=pmeustreo
        # y.append(aux)
    print(y)
    print(termino)
    # Crear el gráfico de dispersión para la señal discreta
    plt.stem(y,termino, basefmt=' ', markerfmt='ro', linefmt='r')

    # Etiquetas y título del gráfico
    plt.xlabel('kt')
    plt.ylabel('X(kt)')
    plt.title('Señal Discreta')

    # Mostrar el gráfico
    plt.show()


def ejecutor(valores_texto,segundo,valores_texto2):
    lista_valores = [float(valor) for valor in valores_texto.split(',') if valor.strip()]
    lista_valores2 = [float(valor) for valor in valores_texto2.split(',') if valor.strip()]
    
    valor_float = float(segundo)
    label3.config(text=ecuacion(lista_valores,valor_float,lista_valores2))
    graficar(lista_valores, lista_valores2)

raiz = Tk()
raiz.title("interfaz perrona")
raiz.geometry("450x450")
raiz.resizable(1,0)


aux1 = StringVar()
aux2 = StringVar()
aux3 = StringVar()

label = Label(text="terminos")
label.place(x=50,y=100)
entry = Entry(textvariable=aux1)
entry.place(x=50,y=150)

label3 = Label(text="terminos 2")
label3.place(x=50,y=250)
entry3 = Entry(textvariable=aux3)
entry3.place(x=50,y=300)


label2 = Label(text="perido de muestreo")
label2.place(x=250,y=100)
entry2 = Entry(textvariable=aux2)
entry2.place(x=250,y=150)

boton = Button(text="graficar",command=lambda:ejecutor(entry.get(),entry2.get(),entry3.get()))
boton.place(x=250,y=300)

label3 = Label(text="")
label3.place(x=0,y=400)



raiz.mainloop()