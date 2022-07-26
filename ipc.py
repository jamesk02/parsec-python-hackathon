import socket
import sys
import atexit
import request as Request
import response as Response

class Ipc:
    server_address = "../quickstart-1.0.0-linux_x86/parsec.sock"
    # usually "/run/parsec/parsec.sock" but we're not on production deployments of parsec
    
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


    def processRequest(self, req):

        toSend = req

        if(type(req) is not bytearray):
            # TODO: toSend = req.build and then serialise
            pass

        self.sock.send(req)
        print("Just sent request to " + self.server_address)

        received = bytearray();

        while(True):
            newReceived = self.sock.recv(36) # may adjust value
            if(newReceived):
                received += bytearray(newReceived)
            else:
                break

        res = received

        if(type(req) is not bytearray):
            # TODO: res = new response object
            pass

        return res


    def destructor(self):
        print("Closing socket")
        self.sock.close()


