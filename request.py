import pickle
import struct
from constants import *
from header import Header
import struct

class Request:
    def __init__(self, opcode, providerId, auth):
        self.opcode = opcode
        self.providerId = providerId
        self.auth = auth
        self.header = Header(self.providerId, self.auth, self.opcode)
        self.body = 1
        self.serialization_type = 'sII'

    def get_header(self):
        return self.header

    def send(self):
        # serialize request and send to parsec
        pass

    def serialize_request(self):
        return struct.pack(self.serialization_type, self.header.serialize(), self.body, self.auth)

    def deserialize_request(self, serialized_request):
        return struct.pack(self.serialization_type, serialized_request)

    