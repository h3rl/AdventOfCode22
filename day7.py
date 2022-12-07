import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test

class Directory:
    def __init__(self,name) -> None:
        self.name = name
        self.children = [] # list of Directory
    
    def add(self, child):
        self.children.append(child)

    def size(self):
        pass

    def getDirByCursor(self, cursor: str):
        
        if cursor == self.name:
            return self
        
        cursor = cursor.split("/") # eg "root/a/b" -> ["root", "a", "b"]
        ncursor = "/".join(cursor[1:])

        for child in self.children:
            if child.name == cursor[1]:
                return child.getDirByCursor(ncursor)
    
    def getSize(self):
        size = 0
        for child in self.children:
            if type(child) == Directory:
                size += child.getSize()
            else:
                size += child.size
        return size

class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = int(size)


def parsedir(dir):
    tot = 0
    for child in dir.children:
        if type(child) == Directory:
            size = child.getSize()
            if size < 100000:
                tot += size
            tot += parsedir(child)
    return tot

def parsedir2(dir, minsize):
    dirs = []
    for child in dir.children:
        if type(child) == Directory:
            size = child.getSize()
            if size > minsize:
                dirs.append(child)
            dirs += parsedir2(child, minsize)
    return dirs

def solve(data):
    root = Directory("root")
    cursor = "root"

    ls_is_next = False

    for line in data:
        # parse line
        line = line.split(" ")
        if line[0] == "$":
            # not in ls mode anymore
            ls_is_next = False
            # command
            if line[1] == "cd":
                # change directory
                new_loc = line[2]
                if new_loc == "/":
                    continue

                if new_loc == "..":
                    # go up
                    cursor = cursor.split("/")
                    cursor = "/".join(cursor[:-1])
                else:
                    cursor += "/" + new_loc
            elif line[1] == "ls":
                # append next lines to current directory
                ls_is_next = True
        elif ls_is_next:
            # ls mode is on
            # this is file or directory
            toappend = None
            if line[0] == "dir":
                # directory
                toappend = Directory(line[1])
                pass
            else:
                toappend = File(line[1], line[0])
                # file
                pass

            # add to root
            root.getDirByCursor(cursor).add(toappend)
    # our dir is ready
    k = parsedir(root)
    print("Solution a: " + str(k))

    #l = parsedir2(root)
    neededspace = 30000000
    freed = 70000000 - root.getSize()
    targetfilesize = (neededspace - freed)
    dirs = parsedir2(root, targetfilesize)

    smallest = None
    for dir in dirs:
        size = dir.getSize()
        if smallest == None or size < smallest:
            smallest = size
            
    print("Solution b: " + str(smallest))
   

def main():
    test_data = parseAOC_test("""\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""")
    data = parseAOC("./day7.txt")

    print("Test data:")
    solve(test_data)
    print("Main data:")
    solve(data)

if __name__ == "__main__":
    main()