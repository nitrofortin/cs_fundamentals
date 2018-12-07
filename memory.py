class Type(object):
    _address_head = None

class Char(Type):
    _bytes = 1

class Short(Type):
    _bytes = 2

class Int(Type):
    _bytes = 4

class Long(Type):
    _bytes = 8

class Array(Type):
    def __init__(self, element_type, size):
        self._bytes = element_type._bytes*size
        self._type = element_type

class Struct(Type):
    def __init__(self, **name_and_type):
        pass

class LinearModel(object):
    def __init__(self, 
                 computer_architecture, 
                 start_address,
                 size):
        self._ca = computer_architecture # big-endian or little-endian 
        self._sa = start_address
        self._size = size

    def read(self, address):
        pass
    def write(self, address, bytes):
        pass
    def hex_dump(self):
        pass