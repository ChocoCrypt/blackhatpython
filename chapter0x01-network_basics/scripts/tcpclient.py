import socket




target_hosts = "192.168.0.109"
target_port = 25565


# AF_INET es para ipv4
# SOCK_STREAM es para un cliente tcp
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)


# Conectarse al servidor
try:
    client.connect((target_hosts, target_port))
    print("connected!")
except:
    print("not connected")
    exit()

# Mandar datos:
client.send(b"something")

# Recibir datos
resp = client.recv(100)
