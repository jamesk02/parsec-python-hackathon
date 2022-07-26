import struct

class Header:
    def default_in(self):
        self.MagicNumber = 0x5EC0A710
        self.HeaderSize = 30
        self.MajorVersionNumber = 1
        self.minorVersionNumber = 0
        self.flags = 0
        self.provider = 0
        self.sessionHandle = 0
        self.contentType = 0
        self.acceptType = 0  #requests only
        self.authType = 0 #requests only
        self.contentLength = 0
        self.authLength = 0
        self.opcode = 1
        self.status = 0 #response only
        self.reserved = 0

        pass

    def __init__(self, provider, sessionHandle, authType, contentLength, opCode, authLength, status):
        self.default_in()

        self.provider = provider
        self.sessionHandle = sessionHandle
        self.authType = authType #only used in requests
        self.contentLength = contentLength        
        self.opcode = opCode

        self.headerSize = 30 #usually fixed
        self.authLength = authLength
        self.status = status
    
    def serialize(self):
        return struct.pack('<IHBBHBQBBBIHIHH',
        self.MagicNumber,
        self.HeaderSize, 
        self.MajorVersionNumber, 
        self.minorVersionNumber, 
        self.flags, 
        self.provider,
        self.sessionHandle, 
        self.contentType,
        self.acceptType,
        self.authType,
        self.contentLength,
        self.authLength,
        self.opcode,
        self.status,
        self.reserved)

    def deserialize(self, serialized_header):
        return struct.unpack('<IHBBHBQBBBIHIHH', serialized_header)