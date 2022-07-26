import numpy as np 

class Response:
    def __init__(self):
        self.MagicNumber = np.uint32(0x5EC0A710)
        self.HeaderSize = np.uint16()  
        self.MajorVersionNumber = np.uint8(0x01)
        self.minorVersionNumber = np.uint8(0x00)
        self.flags = np.uint16(0x00)
        self.provider = np.uint8()
        self.sessionHandle = np.uint64()
        self.contentType = np.uint8(0x00)
        self.acceptType = np.uint8(0x00)
        self.authType = np.uint8()
        self.contentLength = np.uint32()
        self.authLength = np.uint16()
        self.opcode = np.uint32()
        self.status = np.uint16(0x00) #response only
        self.reserved = np.uint16(0x00)

        pass