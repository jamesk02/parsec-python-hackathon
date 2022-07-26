from request import Request
from response import Response
from constants import *
from exceptions import InvalidServiceResponseTypeException

class Client:
    def __init__(self):
        self.ProviderId = ProviderId()
        self.AuthType = AuthType()
        self.Opcodes = Opcodes()

    def ping(self):
        self.processOperation(self.Opcodes.PING,
                              self.ProviderId.CORE,
                              self.AuthType.NO_AUTH)
    
    def listProviders(self):
        res = self.processOperation(self.Opcodes.LIST_PROVIDERS,
                                    self.ProviderId.CORE,
                                    self.AuthType.NO_AUTH)
        return res.body

    def processOperation(self, opcode, providerId, auth):
        req = Request(opcode, providerId, auth)
        req.send()
        res = Response()
        res.receive()

        if res.opcode != opcode:
            raise InvalidServiceResponseTypeException(
                    f"Expected OpCode: {req.opcode} but recieved: {res.opcode}")
        return res