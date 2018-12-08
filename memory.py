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


class Segment(object):
    pass

class Stack(Segment):
    # For fixed size local variables, freed after function call
    pass

class Heap(Segment):
    # Dynamically allocated variables (malloc, free)
    pass

class Static(Segment):
    # global variables, never freed while program runs
    pass

class Code(Segment):
    # store instructions
    pass

class CallStack(Stack):
    def __init__(self):
        self._stack_frames = None
    def put(self, stack_frame):
        self._stack_frames.append(stack_frame)
    def pop(self):
        return self._stack_frames.pop()


class StackFrame(object):
    _function_name = None
    _arguments = None
    _locals = None
    _return_addresses = None
    _cpu_states = None

class MemoryManager(object):
    def allocate_memory(self, size):
        start_address = self._search_memory_chunk(size)
        self._mark_in_use(start_address, size)
        self._memory_repo[start_address] = size
        return start_address

    def free_memory(self, address):
        size = self._memory_repo[address]
        self._mark_as_unused(address, size)
        del self._memory_repo[address]

    def _search_memory_chunk(self, size):
        pass

    def _mark_as_used(self, start, size):
        pass

    def _merge_neighbor_chunks(self):
        pass

class VirtualMemory(object):
    _code = Code()
    _static = Static()
    _stack = Stack()
    _heap = Heap()
    _addresses = {
        _code: None
        _static: None
        _stack: None
        _heap: None
    }

class Process(object):
    _memory_manager = MemoryManager
    _virtual_memory = VirtualMemory
    def __init__(self, pid, exe):
        self.pid = pid
        self.exe = exe

class MemoryPage(object):
    _size = 4096
    def __init__(self, address):
        self._address = address

class MemoryTable(object):
    _entry_size = 4
    _table = {}

    def add_entry(self, virtual, physical):
        v = MemoryPage(virtual)
        p = MemoryPage(physical)
        self._table[v] = p

    def get_physical_address(self, virtual):
        return self._table[virtual]


class Loader(object):
    # load executable in memory
    def create_process(self, exe):
        return Process(exe)

    def get_page_table(self, exe):
        table = MemoryTable()
        virtual, physical = self.get_addresses(exe)
        for v, p in zip(virtual, physical):
            table.add_entry(v, p)
        return table

    def load(self):
        pass
    def _check_os(self):
        pass

    def _check_cpu(self):
        pass


class Kernel(object):
    _loader = Loader()
    _processes = []
    _page_tables = {}

    def spawn_process(self, exe)
        p = self._loader.create_process(exe)
        page_table = self.get_page_table(exe)
        self._page_tables[p] = page_table

    def get_page_table(self, exe):
        table = MemoryTable()
        virtual, physical = self.get_addresses(exe)
        for v, p in zip(virtual, physical):
            table.add_entry(v, p)
        return table

    def get_addresses(self, exe):
        pass