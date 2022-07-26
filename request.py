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
            op_header = Header(0, 1, 0, 0, 1, 0, 0)
            self.header = op_header
            self.body = 1
            self.auth = 0x00

    def get_header(self):
        return self.header

    def send(self):
        pass


if __name__ == "__main__":
    req = Request(1, 0, 0)

    req.build_operation(1)
    
    my_header = req.header
    serialized_header = req.header.serialize()

    print("Serialized header:", serialized_header)
    print(len(serialized_header))

    serialized_full = struct.pack('sII', serialized_header, req.body, req.auth)
    
    deserialized_full = struct.unpack('sII', serialized_full)

    print("Serialized request:", serialized_full)

    deserialized_header = req.header.deserialize(serialized_header)

    print("Deserialized header:", deserialized_header)


    