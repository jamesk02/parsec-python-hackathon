import socket
import sys
import atexit
import request as Request
import response as Response

class Ipc:
    server_address = "/run/parsec/parsec.sock"
    sock = None

    def __init__(self) -> None:
        # Since the "server" in question is parsec itself, we just need to set up client-side stuff
        atexit.register(self.destructor)

        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        try:
            self.sock.connect(self.server_address)
            print("Successfully connected to " + self.server_address)
        except socket.error as err:
            print(err)
            sys.exit()

        # Note: the format for the bytestream for Header/Payload layouts for Requests and Responses
        # are found here https://parallaxsecond.github.io/parsec-book/parsec_client/wire_protocol.html#the-fixed-common-header


    def processRequest(self, request):
        # right now the data doesn't adhere to any of the wire protocol

        self.sock.sendall(request);
        print("Just sent request " + request + " to " + self.server_address) # likely will be gibberish once the request type follows wire protocol

        received = bytearray();

        while(True):
            newReceived = self.sock.recv(1) # may adjust value
            if(newReceived):
                received += bytearray(newReceived)
            else:
                break

        print(received)

        response = Response() # will eventually initialise it with the bytestream
        return response


    def destructor(self):
        print("Closing socket")
        self.sock.close()


