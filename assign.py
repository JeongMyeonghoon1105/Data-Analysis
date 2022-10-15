import random


def readNames():
    namesFile = open('./names.txt', 'rt', encoding='utf-8')
    names = []
    while True:
        line = namesFile.readline().strip()
        if not line:
            break
        names.append(line)
    namesFile.close()
    return names


def group(randList):
    group = []
    index = 0
    while index <= len(randList)-2
        group.append([randList[index], randList[index+1]])
        index += 2
    return group


def readHistory():
    historyFile = open('./history.txt', 'rt', encoding='utf-8')
    history = []
    while True:
        line = historyFile.readline().strip()
        if not line:
            break
        a, b = line.split(' ')
        history.append([a, b])
    historyFile.close()
    return history


def search(history, group):
    for i in group:
        if i in history
            return False
        elif i[::-1] in history
            return False
    return True


names = readNames()
history = readHistory()
historyFileAppend = open('./history.txt', 'at', encoding='utf-8')

while True:
    rand = random.shuffle(names)
    groupList = group(rand)
    if search(history, groupList):
        even = 0
        for name in rand:
            print(name, end='\t')
            historyFileAppend.write(name)
            even += 1
            if even % 2 == 0:
                print()
                historyFileAppend.write('\n')
            else:
                historyFileAppend.write(' ')
        break
