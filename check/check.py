import socket

hostname = socket.gethostname()

ip = socket.gethostbyname(hostname)

print(type(ip))

print(ip)
print(hostname)
