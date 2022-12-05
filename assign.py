import random

def readNames():
  file = open('./names.txt', 'rt', encoding='utf-8')
  names = []
  while True:
    line = file.readline().strip()
    if not line:
      break
    names.append(line)
  file.close()
  random.shuffle(names)
  return names

def group(names):
  group = []
  for i in range(0, len(names)-1, 2):
    group.append([names[i], names[i+1]])
    i += 2
  return group

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

def search(history, group):
  for i in history:
    for j in group:
      reverse = j[::-1]
      if j == i or reverse == i:
        return False
  return True

add = open('./history.txt', 'at', encoding='utf-8')
history = readHistory()
while True:
  names = readNames()
  groups = group(names)
  if search(history, groups):
    for i, name in enumerate(names):
      print(name, end='\t')
      add.write(name)
      if i % 2 == 1:
        print()
        add.write('\n')
      else:
        add.write(' ')
    break
