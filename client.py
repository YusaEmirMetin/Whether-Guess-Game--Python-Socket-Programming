import socket

HOST = 'localhost'
PORT = 8888

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

message = client.recv(1024).decode()
print(message)

attempts = 0

while attempts < 3:
    guess = input("Enter your guess (type 'END' to quit): ")
    client.sendall(guess.encode())

    if guess.upper() == "END":
        print("Connection closed by user.")
        print("Exiting the program...")  
        break

    response = client.recv(1024).decode()
    print(response)

    
    attempts += 1

    
    if "Correct guess" in response:
        break



if attempts == 3 and "Correct guess" not in response:
    
    try:
        extra_msg = client.recv(1024).decode()
        if extra_msg:
            print(extra_msg)
    except:
        pass

client.close()
print("Client program terminated.")
