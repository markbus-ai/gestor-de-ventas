from tkinter import *
import time

file_name = "markbusking_shop.txt"

def mostrar_productos():
    # Mostrar todos los productos
    with open(file_name, "a+") as file:
        file.seek(0)  # Coloca el puntero al inicio del archivo
        objetos = file.read()  # Muestra todo el contenido
        lbl_objetos = Label(ventana_principal,text=objetos,bg="#5FDCC9",fg="black")
        lbl_objetos.place(x="850px", y="0")


#funcion para escribir los objetos en el archivo
def guardar_objeto(name,cantidad,precio):
    with open(file_name, "a+") as file:
        try:
            file.write(f"{name}, {cantidad}, {precio}\n")
            return "producto agregado"
        except:
            return "no se ha podido agregar"


#funcion para definir que objeto agregar al archivo
def agregar_objeto():
    
    #dimensiones de la ventana para escribir el objeto
    ventana_agregar_objeto = Toplevel()
    ventana_agregar_objeto.geometry("250x180")
    
    
    with open(file_name, "a+") as file:
        lbl1 = Label(ventana_agregar_objeto,text="Ingrese el nombre del producto:")
        lbl1.pack()
        #campo donde poner nombre del producto
        name = Entry(ventana_agregar_objeto)
        name.pack()
        
        lbl2 = Label(ventana_agregar_objeto,text="Cantidad vendida: ")
        lbl2.pack()
        
        #campo donde poner la cantidad del producto
        cantidad = Entry(ventana_agregar_objeto)
        cantidad.pack()
        
        lbl3 = Label(ventana_agregar_objeto,text="precio")
        lbl3.pack()
        
        #campo para poner el precio del objeto
        precio = Entry(ventana_agregar_objeto)
        precio.pack()
        
        #boton para escribir todo los datos del objeto en el archivo
        sumbit = Button(ventana_agregar_objeto,text="sumbit", command=lambda: guardar_objeto(name.get(),cantidad.get(),precio.get()))
        sumbit.pack()


def ventana_para_borrar():
    ventana_borrar = Toplevel()
    ventana_borrar.geometry("250x150")
    
    lbl = Label(ventana_borrar,text="Nombre del producto a eliminar")
    lbl.pack()
    
    nombre = Entry(ventana_borrar)
    nombre.pack()
    
    sumbit = Button(ventana_borrar, text="sumbit", command=lambda: eliminar_producto(nombre.get()))
    sumbit.pack()




def eliminar_producto(nombre_producto: str):
    nueva_lista = []
    with open(file_name, "r+") as file:
        lines = file.readlines()
        for line in lines:
            if nombre_producto not in line:
                nueva_lista.append(line)
        # Rebobinar el archivo al inicio
        file.seek(0)
        # Eliminar todas las líneas que contengan el producto
        for line in nueva_lista:
            file.write(line)
        # Eliminar líneas vacías al final del archivo
        file.truncate()

def consultar_producto(name: str, ventana_consulta_producto):
    with open(file_name, "r") as file:
        product_found = False
        for line in file:
            # Verificar si el nombre del producto (sin importar mayúsculas o minúsculas) está presente en la línea
            if name.lower() in line.lower():
                product_found = True
                # Crear un widget Label para mostrar la información del producto
                lbl = Label(ventana_consulta_producto, text=line.strip())
                lbl.pack()
                break  # Salir del bucle después de encontrar una coincidencia

        if not product_found:
            # Mostrar un mensaje si el producto no se encuentra
            no_product_label = Label(ventana_consulta_producto, text="Producto no encontrado")
            no_product_label.pack()
            ventana_principal.after(3000, no_product_label.destroy)


def ventana_consulta_producto():
    ventana_consulta = Toplevel()
    ventana_consulta.geometry("250x150")
    
    lbl = Label(ventana_consulta,text="Nombre del producto")
    lbl.pack()
    
    nombre = Entry(ventana_consulta)
    nombre.pack()
    
    sumbit = Button(ventana_consulta, text="sumbit", command=lambda: consultar_producto(nombre.get(), ventana_consulta))
    sumbit.pack()


def venta_total(ventana_principal):
    # Calcular venta total
    with open(file_name, "r") as file:
        lines = file.readlines()[1:]  # Lee todas las líneas del archivo excepto la primera
        total = 0
        for line in lines:
            columnas = line.strip().split(",")
            cantidad = int(columnas[1])
            precio = float(columnas[2])
            total += cantidad * precio
        venta_label = Label(ventana_principal, text=f"El total es: {total}")
        venta_label.pack()
        
        ventana_principal.after(5000, venta_label.destroy)

def ventana_venta_producto():
    ventana__producto = Toplevel()
    ventana__producto.geometry("200x200")
    
    lbl_producto = Label(ventana__producto, text="Nombre del producto:")
    lbl_producto.pack()
    
    nombre = Entry(ventana__producto)
    nombre.pack()
    
    sumbit = Button(ventana__producto, text="sumbit", command=lambda: venta_producto(nombre.get(), ventana__producto))
    sumbit.pack()


def venta_producto(name,ventana__producto):
    # Calcular venta total
    with open(file_name, "r") as file:
        lines = file.readlines()[1:]  # Lee todas las líneas del archivo excepto la primera
        total = 0
        for line in lines:
            if name in line:
                columnas = line.strip().split(",")
                cantidad = int(columnas[1])
                precio = float(columnas[2])
                total += cantidad * precio
                venta_label = Label(ventana__producto, text=f"El total de {name} es: {total}")
                venta_label.pack()
                return name
        venta_label = Label(ventana__producto, text=f"producto no encontrado")
        venta_label.pack()


def actualizar_producto(nombre_producto,precio,cantidad):
    nueva_lista = []
    with open(file_name, "r+") as file:
        lines = file.readlines()
        for line in lines:
            if nombre_producto not in line:
                nueva_lista.append(line)
        # Rebobinar el archivo al inicio
        file.seek(0)
        # Eliminar todas las líneas que contengan el producto
        for line in nueva_lista:
            file.write(line)
        file.write(f"{nombre_producto}, {cantidad}, {precio}\n")
        # Eliminar líneas vacías al final del archivo
        file.truncate()

def ventana_actualizar_producto():
    ventana_actualizar = Toplevel()
    ventana_actualizar.geometry("200x200")
    
    lbl1 = Label(ventana_actualizar,text="Ingrese el nombre del producto:")
    lbl1.pack()
    #campo donde poner nombre del producto
    name = Entry(ventana_actualizar)
    name.pack()
    
    lbl2 = Label(ventana_actualizar,text="Cantidad vendida: ")
    lbl2.pack()
    
    #campo donde poner la cantidad del producto
    cantidad = Entry(ventana_actualizar)
    cantidad.pack()
    
    lbl3 = Label(ventana_actualizar,text="precio")
    lbl3.pack()
    
    #campo para poner el precio del objeto
    precio = Entry(ventana_actualizar)
    precio.pack()
    
    #boton para escribir todo los datos del objeto en el archivo
    sumbit = Button(ventana_actualizar,text="sumbit", command=lambda: actualizar_producto(name.get(),cantidad.get(),precio.get()))
    sumbit.pack()

def salir():
    ventana_principal.destroy()

ventana_principal = Tk()
ventana_principal.geometry("600x400")
ventana_principal.title("Gestor de productos y ventas")
ventana_principal.config(bg="black")


btn1 = Button(ventana_principal, text="Agregar objeto", command=agregar_objeto)
btn1.place(x="310px",y="26px",height="55px",width="187px")
btn1.config(bg="#56E63D",fg="black")


btn2 = Button(ventana_principal, text="mostrar productos", command=mostrar_productos)
btn2.place(x="505px",y="26px",height="55px",width="187px")
btn2.config(bg="#56E63D",fg="black")

btn3 = Button(ventana_principal, text="eliminar producto", command=ventana_para_borrar)
btn3.place(x="310px",y="118px",height="55px",width="187px")
btn3.config(bg="#56E63D",fg="black")

btn4 = Button(ventana_principal, text="consulta  producto", command=ventana_consulta_producto)
btn4.place(x="505px",y="118px",height="55px",width="187px")
btn4.config(bg="#56E63D",fg="black")

btn5 = Button(ventana_principal, text="venta total", command=lambda: venta_total(ventana_principal))
btn5.place(x="310px",y="210px",height="55px",width="187px")
btn5.config(bg="#56E63D",fg="black")

btn6 = Button(ventana_principal, text="venta por producto", command=ventana_venta_producto)
btn6.place(x="505px",y="210px",height="55px",width="187px")
btn6.config(bg="#56E63D",fg="black")

btn7 = Button(ventana_principal, text="actualizar producto", command=ventana_actualizar_producto)
btn7.place(x="310px",y="302px",height="55px",width="187px")
btn7.config(bg="#56E63D",fg="black")

btn8 = Button(ventana_principal, text="exit", command=salir)
btn8.place(x="505px",y="302px",height="55px",width="187px")
btn8.config(bg="#E63D3D",fg="black")



ventana_principal.mainloop()