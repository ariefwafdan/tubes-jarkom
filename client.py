import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

# Membuat socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect ke server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Request HTTP
request = "GET /index.html HTTP/1.1\r\n"
request += "Host: localhost\r\n"
request += "\r\n"

# Kirim request
client_socket.sendall(request.encode())

# Terima response
response = client_socket.recv(4096).decode()

print("Response dari server:\n")
print(response)

# Tutup koneksi
client_socket.close()
