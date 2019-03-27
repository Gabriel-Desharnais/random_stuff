
import socket
import threading
import pickle

bufferLenght = 1024

class dataTrans:
    def __init__(self,host, port):
        # Create connection
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        process = threading.Thread(target = self.recv )
        process.daemon = True
        process.start()
        self.edit = lambda a,x, justReceived=False: None


    def transmitData(self, data):
        self.s.sendall(pickle.dumps(data))

    def recv(self):
        data = b""
        wait = True
        while True:
            # This loop is meant to  wait for data transmition
            if wait:
                # wait for message to arive
                buff = self.s.recv(bufferLenght)
            else:
                # here to check if data transmition is over
                try:
                    buff = self.s.recv(bufferLenght, socket.MSG_DONTWAIT)
                except BlockingIOError:
                    # The message is over
                    wait = True
                    self.rDataHand(data)
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
                self.rDataHand(data)
                data = b""

    def editDecorator(self, func):
        def wrapper(key, value, justReceived=False):
            if not justReceived:
                self.transmitData((key, value))
            return func(key, value)
        self.edit = wrapper
        return wrapper

    def rDataHand(self, data):
        self.edit(*pickle.loads(data) ,justReceived = True)

    def __del__(self):
        self.s.close()
        del self.s
