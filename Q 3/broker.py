import socket
import threading

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 5010             # Arbitrary non-privileged port
bufferLenght = 1024
connections = []
def acceptConn(s):
    while True:
        conn, addr = s.accept()
        connections.append(conn)
        print('Connected by', addr)
        process = threading.Thread(target = connectionLoop, args=(conn,) )
        process.daemon = True
        process.start()

def connectionLoop(conn):
    with conn:
        data = b""
        wait = True
        while True:
            # This loop is meant to  wait for data transmition
            if wait:
                # wait for message to arive
                buff = conn.recv(bufferLenght)
            else:
                # here to check if data transmition is over
                try:
                    buff = conn.recv(bufferLenght, socket.MSG_DONTWAIT)
                except BlockingIOError:
                    # The message is over
                    wait = True
                    messageHandler(data, conn)
                    data = b""
                    # skip the rest of the loop
                    continue
            if len(buff) == bufferLenght:
                # add data to data
                data += buff
                wait = False
            elif len(buff) == 0:
                # connection closed break loop
                break
            else:
                # Message transmition completed
                data += buff
                wait = True
                messageHandler(data, conn)
                data = b""
            #conn.sendall(data)
        # remove connection from list
        connections.remove(conn)

def messageHandler(data, notme):
    for conn in connections:
        if notme is not conn:
            conn.sendall(data)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
process = threading.Thread(target = acceptConn, args=(s,))
process.daemon = True
process.start()

try:
    while True:
        pass
except:
    s.close()
