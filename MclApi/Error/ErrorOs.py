import MclApi.other.coloful as cl


class MclPathError(Exception):
    def __init__(self,message):
        cl.printRed("MclApi-->PathError")
        super().__init__(message)