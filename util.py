import json
import os.path
import sys
from collections import deque
from urllib.request import urlopen

ALPHABETH = "abcdefghijklmnopqrstuvwxyz"
ALPHABETH_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABETH_FULL = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def parseAOC(path: str) -> list:
    data = readFile(path)
    if len(data) == 1:
        return data[0]
    return data


def parseAOC_test(data, removeempty=False):
    test_data = data.split("\n")

    if test_data[-1] == "":
        test_data.pop()

    if removeempty:
        test_data = removeEmpty(test_data)
    return test_data


def strGridToInts(grid):
    res = []
    for r in grid:
        nc = []
        for c in r:
            if c == " ":
                continue
            nc.append(int(c))
        if len(nc) != 0:
            res.append(nc)
    return res


def readFile(path: str) -> list[str]:
    try:
        abspath = os.path.join(sys.path[0], path)
        file = open(abspath, "r", encoding="utf_8")
        lines = [a.strip() for a in file.readlines()]
        return lines
    except:
        print("file does not exist")


def removeEmpty(array):
    return list(filter(None, array))


def readJson(path: str) -> object:
    try:
        abspath = os.path.join(sys.path[0], path)
        file = open(abspath, "r")
        jsonobj = json.load(file)
        file.close()
        return jsonobj
    except:
        print("file does not exist")


def dumpFile(data: object, path: str) -> None:
    try:
        abspath = os.path.join(sys.path[0], path)
        file = open(abspath, "w")
        json.dump(data, file)
        file.close()
    except:
        print("file does not exist")


def shiftChiper(input: str) -> list[int]:
    inputasnums = []
    for char in input:
        inputasnums.append(ALPHABETH.find(char))

    for k in range(len(ALPHABETH)+1):
        output = ""
        for a in inputasnums:
            if a == -1:
                output += " "
                continue
            output += ALPHABETH[(a+k) % (len(ALPHABETH))]
        print(output)

    return output


def vigenereCihper(input: str, alphabethscount: int = 2) -> None:
    alphabets = []


def getInputFromWeb(day):
    url = f"https://adventofcode.com/2020/day/{day}/input"
    file = urlopen(url)
    print(file.read())
    return
    inputraw = []
    for line in file:
        decoded_line = line.decode("utf-8")
        print(decoded_line)
        inputraw.append(decoded_line)
    return inputraw


def swapxyarray(arr):
    result = []
    for a in arr:
        for j, b in enumerate(a):
            if len(result) <= j:
                result.append(list())
            result[j].append(b)
    return result


def cleanraw(lines):
    return [l.strip() for l in lines]

def strToIntList(arr: list):
    result = [int(intarray) for intarray in arr]
    return result
