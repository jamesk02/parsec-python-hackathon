import pickle
import struct
#from 'constants/auth_types' import AuthTypes
from header import Header
import struct

class Request:
    def __init__(self, opcode, providerId, auth):
        self.opcode = opcode
        self.providerId = providerId
        self.auth = auth
        self.header = None
        self.body = None
        self.auth = None

    def build_operation(self, opcode):
        if opcode == 1:
            op_header = Header(0, 1, 0, 4, 1, 4, 0)
            self.header = op_header
            self.body = 1
            self.auth = 0x00

    def get_header(self):
        return self.header

    def send(self):
        pass




    