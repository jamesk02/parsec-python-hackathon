from request import Request
from response import Response

class Client:
    def __init__(self):
        pass
    def ping(self):
        res = self.processOperation("0x0001", ...)
        if type(res) != PingRes:
            raise InvalidServiceResponseTypeException(f"Expected OpCode: {req.opCode} but recieved: {res.opCode}")
    def processOperation(self, opCode, providerId, auth):
        req = Request(opCode, providerId, auth)
        req.send()
        res = Response()
        res.receive()
        return res