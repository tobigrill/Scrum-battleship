import socket 
import threading


HEADER = 64 #first message to the server must be under 64 bytes (is just to send how long the "real message is")
PORT = 5050 
SERVER = socket.gethostbyname(socket.gethostname()) #gets the ip address of the host-Pc  
#print(SERVER)
ADDR = (SERVER, PORT) #address from the client 
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"
login = "log"
usernamesend = "user"
filename = "users.txt"
online_user= []




server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#creates a socket AF_INET defines it as Ipv4 and SOCK_STREAM ==> TCP
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
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
                online_user.remove(search) 
                print(online_user)  
            print(f"{addr}: {msg}")
            
            if msg == usernamesend:
                for i in range(2):
                    msg_length = conn.recv(HEADER).decode(FORMAT)
                    if msg_length: 
                        msg_length = int(msg_length)
                        msg = conn.recv(msg_length).decode(FORMAT)
                        save(msg)
                        
            if msg == login:
                
                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length: 
                    msg_length = int(msg_length)
                    msg = conn.recv(msg_length).decode(FORMAT)
                    search = msg 
                    
                    with open(filename) as f:
                        for num, line in enumerate(f, 1):
                            if search in line:
                                print(search, "line:" ,num)
                                num += 1
                                pwcompare = f.readline()
                                pwcompare = pwcompare.strip()    
                                
                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length: 
                    msg_length = int(msg_length)
                    msg = conn.recv(msg_length).decode(FORMAT)  
                    pw = msg    
                    #print(f"{pw=} and type = {type(pw)}")
                    #print(f"{pwcompare=} and type = {type(pwcompare)}")
                    if pw == pwcompare:
                        clientwidgetchange = "matchmaking"
                        message = clientwidgetchange.encode(FORMAT)
                        conn.send(message)
                        online_user.append(search)
                        print(online_user)
                    else: 
                        clientError = "wrongPW_BN"
                        message = clientError.encode(FORMAT)
                        conn.send(message)
                        
                            


                    

                
    conn.close()

def save(ud):
    
    userdaten = open(filename,"a")
    userdaten.write(format(ud)+"\n")
    userdaten.close()
    



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