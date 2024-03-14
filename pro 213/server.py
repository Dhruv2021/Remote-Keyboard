import socket
from threading import Thread
from pynput.mouse import Button, Controller as MouseController
from screeninfo import get_monitors
from pynput.keyboard import Key, Controller as KeyboardController

SERVER = None
PORT = 8000
IP_ADDRESS = "192.168.53.242"
screen_width = None
screen_height = None
keyboard = KeyboardController()

def setup():
    print("\n\t\t\t\t\t*** Welcome To Remote Mouse ***\n")
    global SERVER
    global PORT
    global IP_ADDRESS
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(10)
    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...\n")
    getDeviceSize()
    acceptConnections()

def getDeviceSize():
    global screen_width
    global screen_height
    for m in get_monitors():
        screen_width = int(str(m).split(",")[2].strip().split('width=')[1])
        screen_height = int(str(m).split(",")[3].strip().split('height=')[1])

def acceptConnections():
    global SERVER
    while True:
        client_socket, addr = SERVER.accept()
        print(f"Connection established with {addr}")
        thread1 = Thread(target=recvMessages, args=(client_socket,))
        thread1.start()

def recvMessages(client_socket):
    global keyboard
    while True:
        try:
            message = client_socket.recv(2048).decode()
            if message:
                keys = message.split()
                for key in keys:
                    keyboard.press(key)
                    keyboard.release(key)
                    print(key)
        except Exception as e:
            print(f"Error in recvMessages: {e}")

setup()

def acceptConnections():
    global SERVER
    while True:
        client_socket, addr = SERVER.accept ()
        print(f,"Connection established with {client socket}: {addr}")
        thread1 = Thread (target = recvMessage, args=(client_socket,))
        threadl.start()

    setup_thread = threading.Thread(target=setup)                   #sending messages 
    setup_thread.start()        
    

        
def recvMessages(client_socket):
    while True:
        try:
            message = client_socket.recv(2048).decode()
            if message:
                print(f"Key pressed: {message}")
        except Exception as e:
            print(f"Error in recvMessages: {e}")

setup()
acceptConnections()