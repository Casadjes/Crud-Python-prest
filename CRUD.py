import tkinter as tk
from tkinter import messagebox
import os
import datetime

fecha_hora_actual = datetime.datetime.now()
fecha_hora_formateada = fecha_hora_actual.strftime("%d/%m/%Y %H:%M:%S")

def guardar_datos():
    try:
        # Obtener los valores de los campos de entrada
        id_registro = entry_id.get()
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        numero = entry_numero.get()
        puesto = entry_puesto.get()
        monto = entry_monto.get()
        tasa = entry_tasa.get()
        tiempo = entry_tiempo.get()
        pago = "No"

        # Verificar que todos los campos estén completos
        if not id_registro or not nombre or not apellido or not numero or not puesto or not monto or not tasa or not tiempo:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        # Verificar si el ID ya existe
        archivo_datos = "datos.txt"
        if os.path.exists(archivo_datos):
            with open(archivo_datos, "r") as archivo:
                lineas = archivo.readlines()
                for i in range(0, len(lineas), 10):
                    registro_id = lineas[i].strip().split(": ")
                    if len(registro_id) >= 2 and registro_id[1] == id_registro:
                        messagebox.showerror("Error", f"El ID {id_registro} ya está en uso.")
                        return

        # Guardar los datos en el archivo
        with open(archivo_datos, "a") as archivo:
            archivo.write(f"ID: {id_registro}\n")
            archivo.write(f"Nombre: {nombre}\n")
            archivo.write(f"Apellido: {apellido}\n")
            archivo.write(f"Numero: {numero}\n")
            archivo.write(f"Puesto en la empresa: {puesto}\n")
            archivo.write(f"Monto prestado: {monto}\n")
            archivo.write(f"Tasa de interes: {tasa}\n")
            archivo.write(f"Tiempo: {tiempo}\n")
            archivo.write(f"Pago: {pago}\n")
            archivo.write(f"Fecha y hora: {fecha_hora_formateada}\n")
            archivo.write("\n")  # Agregar una línea vacía después de cada usuario

        # Mostrar mensaje de éxito y limpiar los campos de entrada
        messagebox.showinfo("Éxito", "Los datos se han guardado exitosamente.")
        limpiar_campos()
        mostrar_datos()

    except IOError:
        messagebox.showerror("Error", "Error al guardar los datos.")

def cambiar_estado_pago():
    try:
        id_registro = entry_id.get()
        lineas = []

        archivo_datos = "datos.txt"
        if os.path.exists(archivo_datos):
            with open(archivo_datos, "r") as archivo:
                lineas = archivo.readlines()

        with open(archivo_datos, "w") as archivo:
            for i in range(0, len(lineas), 10):
                registro_id = lineas[i].strip().split(": ")
                if len(registro_id) >= 2 and registro_id[1] == id_registro:
                    pago_actual = lineas[i + 8].strip().split(": ")[1]
                    nuevo_pago = "No" if pago_actual == "Si" else "Si"
                    lineas[i + 8] = f"Pago: {nuevo_pago}\n"
                archivo.write("".join(lineas[i:i+10]))

        mostrar_datos()

    except IOError:
        messagebox.showerror("Error", "Error al cambiar el estado de pago.")

def eliminar_datos():
    try:
        id_registro = entry_id.get()
        lineas = []

        archivo_datos = "datos.txt"
        if os.path.exists(archivo_datos):
            with open(archivo_datos, "r") as archivo:
                lineas = archivo.readlines()

        with open(archivo_datos, "w") as archivo:
            for i in range(0, len(lineas), 10):
                registro_id = lineas[i].strip().split(": ")
                if len(registro_id) < 2 or registro_id[1] != id_registro:
                    archivo.write("".join(lineas[i:i+10]))

        messagebox.showinfo("Éxito", "Los datos se han eliminado exitosamente.")
        limpiar_campos()
        mostrar_datos()

    except IOError:
        messagebox.showerror("Error", "Error al eliminar los datos.")

def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_numero.delete(0, tk.END)
    entry_puesto.delete(0, tk.END)
    entry_monto.delete(0, tk.END)
    entry_tasa.delete(0, tk.END)
    entry_tiempo.delete(0, tk.END)

def mostrar_datos():
    try:
        archivo_datos = "datos.txt"
        if os.path.exists(archivo_datos):
            with open(archivo_datos, "r") as archivo:
                lineas = archivo.readlines()

            text_datos.delete(1.0, tk.END)

            for i in range(0, len(lineas), 10):
                if i + 9 < len(lineas):  # Verificar que hay suficientes líneas
                    registro_id = lineas[i].strip().split(": ")
                    if len(registro_id) > 1:
                        registro_id = registro_id[1]
                    else:
                        registro_id = ""
                    
                    nombre = lineas[i + 1].strip().split(": ")
                    if len(nombre) > 1:
                        nombre = nombre[1]
                    else:
                        nombre = ""
                    
                    apellido = lineas[i + 2].strip().split(": ")
                    if len(apellido) > 1:
                        apellido = apellido[1]
                    else:
                        apellido = ""
                    
                    numero = lineas[i + 3].strip().split(": ")
                    if len(numero) > 1:
                        numero = numero[1]
                    else:
                        numero = ""
                    
                    puesto = lineas[i + 4].strip().split(": ")
                    if len(puesto) > 1:
                        puesto = puesto[1]
                    else:
                        puesto = ""
                    
                    monto = lineas[i + 5].strip().split(": ")
                    if len(monto) > 1:
                        monto = monto[1]
                    else:
                        monto = ""
                    
                    tasa = lineas[i + 6].strip().split(": ")
                    if len(tasa) > 1:
                        tasa = tasa[1]
                    else:
                        tasa = ""
                    
                    tiempo = lineas[i + 7].strip().split(": ")
                    if len(tiempo) > 1:
                        tiempo = tiempo[1]
                    else:
                        tiempo = ""
                    
                    pago = lineas[i + 8].strip().split(": ")
                    if len(pago) > 1:
                        pago = pago[1]
                    else:
                        pago = ""
                    
                    fecha_hora = lineas[i + 9].strip()

                    text_datos.insert(tk.END, f"ID: {registro_id}\n")
                    text_datos.insert(tk.END, f"Nombre: {nombre}\n")
                    text_datos.insert(tk.END, f"Apellido: {apellido}\n")
                    text_datos.insert(tk.END, f"Numero de Telefono: {numero}\n")
                    text_datos.insert(tk.END, f"Puesto en la empresa: {puesto}\n")
                    text_datos.insert(tk.END, f"Monto prestado: {monto}\n")
                    text_datos.insert(tk.END, f"Tasa de interes: {tasa}\n")
                    text_datos.insert(tk.END, f"Tiempo: {tiempo}\n")
                    text_datos.insert(tk.END, f"Pago: {pago}\n")
                    text_datos.insert(tk.END, f"Fecha y Hora: {fecha_hora}\n")
                    text_datos.insert(tk.END, "-------------------------------------\n\n")
                else:
                    break
        else:
            text_datos.insert(tk.END, "No hay datos registrados.\n")
    except IOError:
        text_datos.insert(tk.END, "Error al abrir el archivo de datos.\n")

    try:
        archivo_datos = "datos.txt"
        if os.path.exists(archivo_datos):
            with open(archivo_datos, "r") as archivo:
                lineas = archivo.readlines()

            text_datos.delete(1.0, tk.END)

            for i in range(0, len(lineas), 10):
                if i + 9 < len(lineas):  # Verificar que hay suficientes líneas
                    registro_id = lineas[i].strip().split(": ")[1]
                    
                    nombre = lineas[i + 1].strip().split(": ")[1]
                    
                    apellido = lineas[i + 2].strip().split(": ")[1]
                    
                    numero = lineas[i + 3].strip().split(": ")[1]
                    
                    puesto = lineas[i + 4].strip().split(": ")[1]
                    
                    monto = lineas[i + 5].strip().split(": ")[1]
                    
                    tasa = lineas[i + 6].strip().split(": ")[1]
                    
                    tiempo = lineas[i + 7].strip().split(": ")[1]
                    
                    pago = lineas[i + 8].strip().split(": ")[1]
                    
                    fecha_hora = lineas[i + 9].strip()

                    text_datos.insert(tk.END, f"ID: {registro_id}\n")
                    text_datos.insert(tk.END, f"Nombre: {nombre}\n")
                    text_datos.insert(tk.END, f"Apellido: {apellido}\n")
                    text_datos.insert(tk.END, f"Numero de Telefono: {numero}\n")
                    text_datos.insert(tk.END, f"Puesto en la empresa: {puesto}\n")
                    text_datos.insert(tk.END, f"Monto prestado: {monto}\n")
                    text_datos.insert(tk.END, f"Tasa de interes: {tasa}\n")
                    text_datos.insert(tk.END, f"Tiempo: {tiempo}\n")
                    text_datos.insert(tk.END, f"Pago: {pago}\n")
                    text_datos.insert(tk.END, f"Fecha y Hora: {fecha_hora}\n")
                    text_datos.insert(tk.END, "-------------------------------------\n\n")
                else:
                    break
        else:
            text_datos.insert(tk.END, "No hay datos registrados.\n")
    except IOError:
        text_datos.insert(tk.END, "Error al abrir el archivo de datos.\n")





# Crear la ventana principal
window = tk.Tk()
window.title("CRUD")
window.geometry("850x600")

# Etiquetas
label_id = tk.Label(window, text="ID:", font=("Arial", 12, "bold"))
label_id.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

label_nombre = tk.Label(window, text="Nombre:", font=("Arial", 12, "bold"))
label_nombre.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

label_apellido = tk.Label(window, text="Apellido:", font=("Arial", 12, "bold"))
label_apellido.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

label_numero = tk.Label(window, text="Número:", font=("Arial", 12, "bold"))
label_numero.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

label_puesto = tk.Label(window, text="Puesto en la empresa:", font=("Arial", 12, "bold"))
label_puesto.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

label_monto = tk.Label(window, text="Monto prestado:", font=("Arial", 12, "bold"))
label_monto.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)

label_tasa = tk.Label(window, text="Tasa de interés:", font=("Arial", 12, "bold"))
label_tasa.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)

label_tiempo = tk.Label(window, text="Tiempo:", font=("Arial", 12, "bold"))
label_tiempo.grid(row=7, column=0, padx=10, pady=10, sticky=tk.W)

# Campos de entrada
entry_id = tk.Entry(window)
entry_id.grid(row=0, column=1, padx=10, pady=10)

entry_nombre = tk.Entry(window)
entry_nombre.grid(row=1, column=1, padx=10, pady=10)

entry_apellido = tk.Entry(window)
entry_apellido.grid(row=2, column=1, padx=10, pady=10)

entry_numero = tk.Entry(window)
entry_numero.grid(row=3, column=1, padx=10, pady=10)

entry_puesto = tk.Entry(window)
entry_puesto.grid(row=4, column=1, padx=10, pady=10)

entry_monto = tk.Entry(window)
entry_monto.grid(row=5, column=1, padx=10, pady=10)

entry_tasa = tk.Entry(window)
entry_tasa.grid(row=6, column=1, padx=10, pady=10)

entry_tiempo = tk.Entry(window)
entry_tiempo.grid(row=7, column=1, padx=10, pady=10)

# Botones
btn_guardar = tk.Button(window, text="Guardar", command=guardar_datos, bg="#66CC66")
btn_guardar.grid(row=9, column=0, padx=10, pady=10)

btn_cambiar_pago = tk.Button(window, text="Cambiar estado de pago", command=cambiar_estado_pago, bg="#6699CC")
btn_cambiar_pago.grid(row=9, column=1, padx=10, pady=10)

btn_eliminar = tk.Button(window, text="Eliminar", command=eliminar_datos,  bg="#FF6666")
btn_eliminar.grid(row=9, column=2, padx=10, pady=10)

# Área de texto
text_datos = tk.Text(window, width=60, height=30)
text_datos.grid(row=0, column=2, rowspan=9, padx=10, pady=10)

# Mostrar los datos existentes
mostrar_datos()

# Ejecutar la ventana principal
window.mainloop()
