from tkinter import *

master=None

container_principal = Frame(master)
container_principal["pady"]=5
container_principal.pack()

container2 = Frame(master)
container2["padx"]=20
container2["pady"]=5
container2.pack()

container3 = Frame(master)
container3["padx"]=20
container3["pady"]=5
container3.pack()

titulo = Label( container_principal, text="Rotação de imagens" )
titulo.pack()

lbl_graus = Label(container2, text="Informe quantos graus para girar:", width=30)
lbl_graus.pack( side= LEFT )

txt_graus = Entry(container2)
txt_graus["width"]=10
txt_graus.pack( side=LEFT)

btn = Button(container3, text="Selecionar imagem")
btn.pack( side=LEFT)


