import socket
import threading
import time

PORT = 8080

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', PORT))
    server_socket.listen(1)
    print("Server listening on port", PORT)
    
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")
    
    buffer = client_socket.recv(1024).decode()
    print(f"Server received: {buffer}")
    
    hello = "Hello from server"
    client_socket.send(hello.encode())
    print("Hello message sent from server")
    
    client_socket.close()
    server_socket.close()

def run_client():
    time.sleep(1)  # Wait for the server to start
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect(('127.0.0.1', PORT))
    except ConnectionRefusedError:
        print("Connection failed. Is the server running?")
        return
    
    hello = "Hello from client"
    client_socket.send(hello.encode())
    print("Client: Hello message sent")
    
    buffer = client_socket.recv(1024).decode()
    print(f"Client received: {buffer}")
    
    client_socket.close()

# Create and start the server thread
server_thread = threading.Thread(target=run_server)
server_thread.start()

# Allow some time for the server to start
time.sleep(1)

# Run the client
run_client()

# Wait for the server thread to complete
server_thread.join()