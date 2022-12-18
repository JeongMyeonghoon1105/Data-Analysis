import os
os.remove('./requires.txt')

def readNames():
  file = open('./names.txt', 'rt', encoding='utf-8')
  names = []
  while True:
    line = file.readline().strip()
    if not line:
      break
    names.append(line)
  file.close()
  return names

def readHistory():
  file = open('./history.txt', 'rt', encoding='utf-8')
  history = []
  while True:
    line = file.readline().strip()
    if not line:
      break
    a, b = line.split(' ')
    history.append([a, b])
  file.close()
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
    checked.append(i)
