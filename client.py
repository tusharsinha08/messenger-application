import socket
import threading

HOST = '127.0.0.1'
PORT = 1234



def listen_for_message_from_server(client):
    
    while 1:

        message = client.recv(2028).decode('utf-8')
        if message != '':
            print(f"{message}")
        else:
            print("Message received from client is empty")


def send_message_to_server(client, username):
    print("Now you can chat: ")
    while 1:
        message = input()
        if message != '':
            full_message = f"[{username}] >> {message}"
            client.sendall(full_message.encode())
        else:
            print("Empty message")
            exit(0)



def communicate_to_server(client):
    username = input("Enter username: ")
    if username != '':
        client.sendall(username.encode())
    else:
        print("Username can't be empty")
        exit(0)
    
    threading.Thread(target=listen_for_message_from_server, args=(client, )).start()

    send_message_to_server(client, username)



def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    try:
        client.connect((HOST, PORT))
        print(f"Successfully connected to server")
    except:
        print(f"Unable to connect to server {HOST}  {PORT}")
    
    communicate_to_server(client)

if __name__ == '__main__':
    main()