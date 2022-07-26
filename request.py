import pickle
import struct
from header import Header

class Request:
    def __init__(self, opcode, providerId, auth):
        self.opcode = opcode
        self.providerId = providerId
        self.auth = auth
        self.header = None

    def build_operation(self, opcode):
        if opcode == 1:
            op_header = Header(0, 1, 0, 0, 1)
            self.header = op_header

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
    
    deserialized_header = req.header.deserialize(serialized_header)

    print("Deserialized header:", deserialized_header)
    