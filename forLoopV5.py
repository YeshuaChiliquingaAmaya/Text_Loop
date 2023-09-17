import time
import tkinter as tk
from tkinter import simpledialog
import keyboard

def send_message():
    message = entry.get("1.0", "end-1c")  # Obtiene el texto del cuadro de texto
    number_value = simpledialog.askinteger("Input", "Enter the number of times to send the message:")

    if message and number_value:
        # Elimina los saltos de línea del mensaje
        message = message.replace('\n', ' ')

        time.sleep(2)

        for i in range(number_value):
            keyboard.write(message)
            keyboard.press_and_release('Enter')

# Configura la ventana
root = tk.Tk()
root.title("Message Sender")

# Ajusta el tamaño del cuadro de texto (height y width)
entry = tk.Text(root, height=20, width=80)  # Puedes cambiar estos valores según tus necesidades
entry.pack(padx=10, pady=10)

# Crea un botón para enviar el mensaje
send_button = tk.Button(root, text="Send Message", command=send_message)
send_button.pack(pady=10)

# Ejecuta la interfaz gráfica
root.mainloop()
