
import ipc
import request
import response

from header import Header
import struct

import binascii

if __name__ == "__main__":
    ipc = ipc.Ipc()

    req = request.Request(1, 0, 0)

    req.build_operation(1)
    
    my_header = req.header
    serialized_header = req.header.serialize()

    print("Serialized header:", serialized_header)
    print(len(serialized_header))

    serialized_full = struct.pack('36sII', serialized_header, req.body, req.auth)
    
    deserialized_full = struct.unpack('36sII', serialized_full)

    print("Serialized request:", serialized_full)

    deserialized_header = req.header.deserialize(serialized_header)

    print("Deserialized header:", deserialized_header)

    res = ipc.processRequest(serialized_full)

    print(binascii.hexlify(res))