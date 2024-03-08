import socket
def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345) # Replace 'localhost' with your IP address
    server_socket.bind(server_address)
    server_socket.listen(1) # max number of clients

    print ("Server listening for incoming connections...")

    while True:
        # Wait for connection
        client_socket, client_address = server_socket.accept() 

        try:
            print("Connection to:", client_address)

            # Receive data from client
            data = client_socket.recv(1024) #size of message to receive; 1024 is maximum
            print("Received:", data.decode())

            # Send acknowledgement back to client
            message = "Message received by the server!"
            client_socket.sendall(message.encode())

        finally:
            # Clean up connection
            client_socket.close()

if __name__ == "__main__":
    run_server()