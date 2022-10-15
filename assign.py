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
    random.shuffle(names)
    return names

def group(randList):
    group = []
    index = 0
    while True:
        if index > len(randList)-2:
            break
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
    for i in history:
        for k in group:
            reverse = k[::-1]
            if k == i or reverse == i:
                return False
    return True


historyFileAppend = open('./history.txt', 'at', encoding='utf-8')
history = readHistory()
while True:
    rand = readNames()
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
