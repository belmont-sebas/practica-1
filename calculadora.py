import tkinter as tk

def agregar_caracter(caracter):
    entrada.insert(tk.END, caracter)

def limpiar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        resultado_label.config(text="Resultado: " + str(resultado))
    except Exception as e:
        resultado_label.config(text="Error al calcular")

# Configuración de la ventana
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x400")
root.configure(bg="#7E57C2")

# Entrada
entrada = tk.Entry(root, width=20, font=("Arial", 16))
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones de números y operaciones
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for texto, fila, columna in botones:
    boton = tk.Button(root, text=texto, width=5, height=2, font=("Arial", 12), bg="#BA68C8", fg="white",
                      command=lambda t=texto: agregar_caracter(t) if t != "C" else limpiar() )
    boton.grid(row=fila, column=columna, padx=5, pady=5)

# Botón de calcular
calcular_btn = tk.Button(root, text="Calcular", width=10, height=2, font=("Arial", 12), bg="#BA68C8", fg="white",
                         command=calcular)
calcular_btn.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# Resultado
resultado_label = tk.Label(root, text="Resultado: ", font=("Arial", 14), bg="#7E57C2", fg="white")
resultado_label.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()

