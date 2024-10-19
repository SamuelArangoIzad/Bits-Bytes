import tkinter as tk
from tkinter import messagebox
from Level1.Code import code
class Init:

    def __init__(self, root):
        self.root = root
        self.root.title("Conversión Binaria - Menú Dinámico")
        self.create_menu()

    def create_menu(self):
        label = tk.Label(self.root, text="Selecciona una opción:")
        label.pack()

        # Botón para convertir texto a binario
        btn_to_bin = tk.Button(self.root, text="Convertir texto a binario", command=self.text_to_bin)
        btn_to_bin.pack(pady=5)

        # Botón para convertir binario a texto
        btn_to_text = tk.Button(self.root, text="Convertir binario a texto", command=self.bin_to_text)
        btn_to_text.pack(pady=5)

        # Botón para salir del programa
        btn_exit = tk.Button(self.root, text="Salir", command=self.root.quit)
        btn_exit.pack(pady=5)

    def text_to_bin(self):
        # Crear una nueva ventana para la entrada de texto
        input_window = tk.Toplevel(self.root)
        input_window.title("Texto a Binario")

        label = tk.Label(input_window, text="Introduce el texto:")
        label.pack()

        input_text = tk.Entry(input_window)
        input_text.pack()

        def translate():
            text = input_text.get()
            if text:
                binario = code.string_to_bits(text)
                messagebox.showinfo("Resultado", f"Binario: {binario}")
            else:
                messagebox.showerror("Error", "Por favor, introduce un texto válido.")

        btn_convert = tk.Button(input_window, text="Convertir", command=translate)
        btn_convert.pack(pady=5)

    def bin_to_text(self):
        # Crear una nueva ventana para la entrada de binario
        input_window = tk.Toplevel(self.root)
        input_window.title("Binario a Texto")

        label = tk.Label(input_window, text="Introduce el binario (8 bits por carácter):")
        label.pack()

        input_bits = tk.Entry(input_window)
        input_bits.pack()

        def translate():
            bits = input_bits.get()
            if all(c in '01' for c in bits) and len(bits) % 8 == 0:
                texto = code.bits_to_string(bits)
                messagebox.showinfo("Resultado", f"Texto: {texto}")
            else:
                messagebox.showerror("Error", "Por favor, introduce una cadena binaria válida.")

        btn_convert = tk.Button(input_window, text="Convertir", command=translate)
        btn_convert.pack(pady=5)

# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Init(root)
    root.mainloop()
