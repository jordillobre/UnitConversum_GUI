import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("UnitConvertum")
ventana.geometry("600x600")

# ----- FRAME SUPERIOR -----
frame_superior = tk.Frame(ventana, bg="lightblue", bd=5)
frame_superior.pack(side="top", fill="x", padx=10, pady=10)

# Lista desplegable
opciones = ["Opción 1", "Opción 2", "Opción 3"]
combo = ttk.Combobox(frame_superior, values=opciones, state="readonly")
combo.current(0)  # Selección inicial
combo.pack(pady=10)

# ----- FRAME INFERIOR -----
frame_inferior = tk.Frame(ventana, bg="red", bd=5)
frame_inferior.pack(side="top", fill="x", padx=10, pady=10)

# Función del botón
def ejecutar_accion():
    seleccion = combo.get()
    print("Has seleccionado:", seleccion)
    # Aquí pones el código según la selección

# Botón en el frame inferior
boton = tk.Button(frame_inferior, text="Convertir", bg="white", fg="black", command=ejecutar_accion)
boton.pack(pady=10)

ventana.mainloop()
