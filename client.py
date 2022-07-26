from request import Request
from response import Response
from constant import *
from exceptions import InvalidServiceResponseTypeException

class Client:
    def __init__(self):
        self.providerId = ProviderId()
        self.authType = AuthType()
        self.opcodes = Opcodes()

    def ping(self):
        self.processOperation(self.opcodes.PING, self.providerId.CORE, self.authType.NO_AUTH)
    
    def listProviders(self):
        res = self.processOperation(self.opcodes.LIST_PROVIDERS, self.providerId.CORE, self.authType.NO_AUTH)
        return res.body

    def processOperation(self, opcode, providerId, auth):
        req = Request(opcode, providerId, auth)
        req.send()
        res = Response()
        res.receive()

        if res.opcode != opcode:
            raise InvalidServiceResponseTypeException(f"Expected OpCode: {req.opCode} but recieved: {res.opCode}")
        return res