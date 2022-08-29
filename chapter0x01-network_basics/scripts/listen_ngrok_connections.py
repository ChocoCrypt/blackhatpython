"""
Simple scripts that grabs all the connections recived by people scanning ngrok
"""
import socket
import sys
import threading
import datetime



ip = "0.0.0.0"
port  = int(sys.argv[1])

# Defino mi servidor
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind((ip,port))
server.listen(5)
print(f"listening on {port}")



def manejar_requets(client_socket):

    request = client_socket.recv(2048)
    print(f"llegó {request}")
    # Contesto
    client_socket.send(b"Buena papi esto lo guardare")
    fecha = str(datetime.datetime.now()).replace(" ","")
    with open(f"{fecha}.req","w") as fp:
        data = str(request)
        fp.write(data)
    client_socket.close()


if __name__ == "__main__":
    while(True):
        client, addr = server.accept()
        print(f"llegó un request desde {addr}")
        client_handler = threading.Thread(target= manejar_requets , args =(client,))
        client_handler.start()
