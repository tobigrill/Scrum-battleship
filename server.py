import socket 
import threading

HEADER = 64 #first message do the server must be bytes 64 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #gets the ip address of the host-Pc 
#print(SERVER)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creates a socket 
server.bind(ADDR)

def handle_client(conn, addr):#runs for each client (alsways in a new thread)
    print(f"New Connection {addr} connected" )
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length: 
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False 
            
        
            print(f"{addr}: {msg}")
            conn.send("Msg received".encode(FORMAT))
        
    conn.close()


def start():#handels new conections
    server.listen() #serverlistens aslong as their is no crash or something else happen 
    print(f"Serveraddresse {SERVER}")
    while True:
        conn, addr = server.accept()  #stores the addr of clients an a Object do send information back(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"ACTIVE CONNECTIONS:{threading.activeCount()-1}")

print("Server is starting...")
start()