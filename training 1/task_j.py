import sys
import re

class Namespace:
    def __init__(self):
        self.storage = {}

    def get(self, name):
        return self.storage.get(name)

    def set(self, name, value):
        self.storage[name] = value

class GenericList:
    def get(self, i):
        pass

    def set(self, i, value):
        pass

    def sublist(self, from_, to_):
        pass

    def length(self):
        pass

    def add(self, value):
        raise NotImplementedError("Add is only available for root lists.")

class List(GenericList):
    def __init__(self, data):
        self.data = data
        self.is_root_list = True

    def get(self, i):
        return self.data[i]

    def set(self, i, value):
        self.data[i] = value

    def add(self, value):
        if not self.is_root_list:
            raise NotImplementedError("Add is only available for root lists.")
        self.data.append(value)

    def sublist(self, from_, to_):
        return Sublist(self, from_, to_)

    def length(self):
        return len(self.data)

class Sublist(GenericList):
    def __init__(self, parent, start, end):
        self.parent = parent
        self.start = start
        self.end = end
        self.is_root_list = False

    def get(self, i):
        if i < 0 or i >= self.length():
            raise IndexError("Index out of bounds")
        return self.parent.get(self.start + i)

    def set(self, i, value):
        if i < 0 or i >= self.length():
            raise IndexError("Index out of bounds")
        self.parent.set(self.start + i, value)

    def sublist(self, from_, to_):
        if from_ < 0 or to_ >= self.length() or from_ > to_:
            raise IndexError("Invalid sublist range")
        return Sublist(self.parent, self.start + from_, self.start + to_)

    def length(self):
        return self.end - self.start + 1

    def add(self, value):
        raise NotImplementedError("Add is only available for root lists.")

def execute_command(line, memory):
    line = line.strip()

    if line.startswith("List ") and "= new List(" in line:
        m = re.match(r"List (\w+) = new List\((.*)\)", line)
        if not m:
            raise ValueError(f"Invalid new List syntax: {line}")
        name, values_str = m.groups()
        values = list(map(int, values_str.split(","))) if values_str else []
        memory.set(name, List(values))

    elif line.startswith("List ") and ".subList(" in line:
        m = re.match(r"List (\w+) = (\w+)\.subList\((\d+),(\d+)\)", line)
        if not m:
            raise ValueError(f"Invalid subList syntax: {line}")
        new_name, source_name, start, end = m.groups()
        source = memory.get(source_name)
        if source is None:
            raise Exception(f"List '{source_name}' not found")
        
        start_0based = int(start) - 1
        end_0based = int(end) - 1
        
        if (start_0based < 0 or end_0based >= source.length() or 
            start_0based > end_0based):
            raise IndexError(f"Invalid sublist range: {start}-{end} for list of length {source.length()}")
        
        memory.set(new_name, source.sublist(start_0based, end_0based))

    elif ".get(" in line:
        m = re.match(r"(\w+)\.get\((\d+)\)", line)
        if not m:
            raise ValueError(f"Invalid get syntax: {line}")
        name, index = m.groups()
        lst = memory.get(name)
        if lst is None:
            raise Exception(f"List '{name}' not found")
        # Конвертируем 1-based индекс в 0-based
        index_0based = int(index) - 1
        if index_0based < 0 or index_0based >= lst.length():
            raise IndexError(f"Index {index} out of bounds for list of length {lst.length()}")
        print(lst.get(index_0based))

    elif ".set(" in line:
        m = re.match(r"(\w+)\.set\((\d+),(\d+)\)", line)
        if not m:
            raise ValueError(f"Invalid set syntax: {line}")
        name, index, value = m.groups()
        lst = memory.get(name)
        if lst is None:
            raise Exception(f"List '{name}' not found")
        # Конвертируем 1-based индекс в 0-based
        index_0based = int(index) - 1
        if index_0based < 0 or index_0based >= lst.length():
            raise IndexError(f"Index {index} out of bounds for list of length {lst.length()}")
        lst.set(index_0based, int(value))

    elif ".add(" in line:
        m = re.match(r"(\w+)\.add\((\d+)\)", line)
        if not m:
            raise ValueError(f"Invalid add syntax: {line}")
        name, value = m.groups()
        lst = memory.get(name)
        if lst is None:
            raise Exception(f"List '{name}' not found")
        lst.add(int(value))

    else:
        raise ValueError(f"Unrecognized command: {line}")

def main():
    n = int(sys.stdin.readline())
    memory = Namespace()
    for _ in range(n):
        line = sys.stdin.readline()
        execute_command(line, memory)

if __name__ == "__main__":
    main()