from request import Request
from response import Response
from constants import *
from exceptions import InvalidServiceResponseTypeException
import struct

class Client:
    def __init__(self):
        self.ProviderIds = ProviderIds()
        self.AuthType = AuthType()
        self.Opcodes = Opcodes()

    def ping(self):
        self.processOperation(self.Opcodes.PING,
                              self.ProviderIds.CORE,
                              self.AuthType.NO_AUTH)
    
    def listProviders(self):
        res = self.processOperation(self.Opcodes.LIST_PROVIDERS,
                                    self.ProviderIds.CORE,
                                    self.AuthType.NO_AUTH)
        # Output the list of providers here according to the response. Maybe return res.data??

    def processOperation(self, opcode, providerId, authType):
        req = Request(opcode, providerId, authType)
        req.send()
        res = Response()
        res.receive()

        if res.opcode != opcode:
            raise InvalidServiceResponseTypeException(
                    f"Expected Opcode: {req.opcode} but recieved: {res.opcode}")
        return res