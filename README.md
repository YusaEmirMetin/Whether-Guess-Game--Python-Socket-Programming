Mini Weather Prediction (TCP)

### 🧾 Overview
This project simulates a weather guessing game using **TCP socket communication** between a Python-based client and server. The server randomly selects a city and temperature from an Excel file, and the client tries to guess the temperature within a 10% tolerance range.

### 🛠 Technologies Used
- Python 3.x  
- `socket` module  
- `pandas` for Excel reading  
- Excel file: `weathers.xlsx`

### 🧠 Features
- Client-server communication via TCP (localhost, port `8888`)
- Server picks a random city from `weathers.xlsx`
- Client has 3 attempts to guess the temperature
- Real-time feedback from server:
  - Correct guess
  - Too high / Too low hints
  - Invalid input handling
  - Manual termination with `END`
- Graceful shutdown of connection

### 🗃 Files
- `server.py`  
- `client.py`  
- `weathers.xlsx`  
- `CMPE 472 Assigment1 Report.docx`

---

## 📘 Assignment 2: UDP Pinger Simulation (Simulated UDP Behavior)

### 🧾 Overview
This simulation mimics a **UDP-like socket interaction** without using the actual socket library. Two Python classes (`Servermy` and `Clientmy`) are defined to simulate connection creation, validation, and message exchange.

### 📌 Simulation Focus
- No actual socket library used  
- Domain number, type number, and protocol number must be `4`, `1`, `1` respectively  
- Port number must be `9000` to allow "connection"  
- Simulated messages: `Hello`, `Access9000`, `Access5000`, `End`, etc.

### ⚙️ Components

#### Servermy
- `__init__`: Initializes server attributes  
- `socketcreator()`: Validates domain/type/protocol  
- `serveraccept()`: Accepts client based on port number  
- `serverreader(message)`: Responds to client messages

#### Clientmy
- `__init__`: Initializes client attributes  
- `clientcreator()`: Validates domain/type/protocol  
- `clientconnect()`: Asks user for port number  
- `clientwriter()`: Sends messages to server

### 🔄 Interaction Simulation
- Client sends a message (e.g., `Access5000`)
- Server decides whether to respond, reject, or terminate based on message type and port
- No real socket; logic is hard-coded simulation

### 🗃 Files
- `main.py`  
- `CMPE472 HW2.pdf`

---

## 📝 How to Run

### Assignment 1
```bash
# Open two terminals
python server.py   # Terminal 1
python client.py   # Terminal 2
