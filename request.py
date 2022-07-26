class Request:
    def __init__(self, opcode, providerId, auth):
        self.opcode = opcode
        self.providerId = providerId
        self.auth = auth
    def send(self):
        pass