import socket
import random
import pandas as pd

file_path = 'weathers.xlsx'
df = pd.read_excel(file_path)

HOST = 'localhost'
PORT = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"Server listening on {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    print(f"Connected by {addr}")

    selected_row = df.sample().iloc[0]
    city = selected_row['City']
    temp = selected_row['Temp']

    conn.sendall(f"Guess the temperature for {city}\n".encode())

    attempts = 0             
    invalid_inputs = 0       
    tolerance = 0.1 * temp
    guessed_correctly = False

    while attempts < 3:
        guess = conn.recv(1024).decode().strip()

        if guess.upper() == "END":
            conn.sendall("Connection closed by user.\n".encode())
            conn.close()
            print("Shutting down the server...")
            server.close()
            exit()

        try:
            val = float(guess)
        except ValueError:
            invalid_inputs += 1
            if invalid_inputs == 3:
                conn.sendall("Too many invalid inputs. Terminating connection.\n".encode())
                conn.close()
                break
            conn.sendall("Invalid input. Please enter a number.\n".encode())
            continue

        attempts += 1

        if (temp - tolerance) <= val <= (temp + tolerance):
            conn.sendall("Congratulations! Correct guess.\n".encode())
            guessed_correctly = True
            break
        elif val < temp:
            conn.sendall("Try a higher value.\n".encode())
        else:
            conn.sendall("Try a lower value.\n".encode())

    if not guessed_correctly and attempts == 3:
        conn.sendall(f"Your attempts are over. The correct temperature was: {temp}\n".encode())

    conn.close()
