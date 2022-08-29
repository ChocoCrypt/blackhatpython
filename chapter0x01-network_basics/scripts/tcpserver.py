import socket
import threading


bind_ip = "0.0.0.0"
bind_port = 1234

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)


server.bind((bind_ip , bind_port))
server.listen(5)
print(f"server is listening on {bind_port}")

def handle_client(client_socket):
    req = client_socket.recv(1024)
    print(f"se recibio {req}")
    # Ahora se le responde al cliente
    client_socket.send(b"buena papi")
    client_socket.close()

while(True):
    client,addr = server.accept()
    print(f"llegó {client} desde {addr}")
    client_handler = threading.Thread(target = handle_client , args=(client, ))
    client_handler.start()
