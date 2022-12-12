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

names = readNames()
history = readHistory()
requiresAppend = open('./requires.txt', 'at', encoding='utf-8')
checked = []

for i in names:
    matched = []
    for j in history:
        if j[0] == i:
            matched.append(j[1])
        elif j[1] == i:
            matched.append(j[0])
    for j in names:
        if j not in matched and i != j and j not in checked:
            requiresAppend.write(i + ' ' + j + '\n')
            print(i, end=' ')
            print(j)
    checked.append(i)