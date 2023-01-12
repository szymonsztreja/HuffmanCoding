# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import Counter, OrderedDict
# from Letter import Letter.Letter()


class OrderedCounter(Counter, OrderedDict):
    pass


def min_heapify(array, i):
    leftChildIndex = 2 * i + 1
    rightChildIndex = 2 * i + 2

    if leftChildIndex < len(array) and array[leftChildIndex][1] < array[i][1]:
        smallest = leftChildIndex
    else:
        smallest = i

    if rightChildIndex < len(array) and array[rightChildIndex][1] < array[smallest][1]:
        smallest = rightChildIndex

    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)


def min_heap(listt):
    for i in range(len(listt)//2 - 1, -1, -1):
        min_heapify(listt, i)


def huffman():
    f = open("fileToCompress.txt", "r")
    text = f.read()
    counter = OrderedCounter(text)
    tuples = list(counter.items())
    listt = [list(x) for x in tuples]
    for x in range(len(listt), 1, -1):
        min_heap(listt)
        extracted1 = extract_min(listt)
        min_heap(listt)
        extracted2 = extract_min(listt)
        insertion = [extracted1[0] + extracted2[0], extracted1[1] + extracted2[1]]
        insert(listt, insertion)
        letter = Letter(extracted1[0], extracted1[1], 0)
        print(letter)
aaa
    print(listt)


def extract_min(array):
    return array.pop(0)


def insert(array2d, insertion):
    array2d.append(insertion)


class Letter:
    def __init__(self, letter, letter_count, code):
        self.letter = letter
        self.letter_count = letter_count
        self.code = code


if __name__ == '__main__':
    huffman()


