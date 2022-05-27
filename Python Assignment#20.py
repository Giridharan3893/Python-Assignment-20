#!/usr/bin/env python
# coding: utf-8

# In[7]:


##Answer1:

df = open("Giri.txt")

read = df.read()

df.seek(0)
read


# In[8]:


##Answer2:

file = open("Giri2.txt","r")
Counter = 0

Content = file.read()
CoList = Content.split("\n")
  
for i in CoList:
    if i:
        Counter += 1
          
print("This is the number of lines in the file")
print(Counter)


# In[10]:


##Answer3:

file1 = open('Giri3.txt',
             'r')

file2 = open('Giri3Updated.txt',
             'w')

for line in file1.readlines():

    if not (line.startswith('Python')):

        print(line)

        file2.write(line)

file2.close()
file1.close()


# In[13]:


##Answer4:

outputFile = open('Giri3.txt', "w")

inputFile = open('Giri3.txt', "r")

lines_seen_so_far = set()

for line in inputFile:

    if line not in lines_seen_so_far:

        outputFile.write(line)

        lines_seen_so_far.add(line)        

inputFile.close()
outputFile.close()


# In[14]:


##Answer5:

def parse(d):
    dictionary = dict()
   
    pairs = d.strip('{}').split(', ')
    for i in pairs:
        pair = i.split(': ')
        
        dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
    return dictionary
try:
    tetx_file = open('Giri5.txt', 'rt')
    lines = geeky_file.read().split('\n')
    for l in lines:
        if l != '':
            dictionary = parse(l)
            print(dictionary)
    geeky_file.close()
except:
    print("Something unexpected occurred!")


# In[15]:


##Answer6:

firstfile = input("Enter the name of first file ")
secondfile = input("Enter the name of second file ")

f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')

print('content of first file before appending -', f1.read())
print('content of second file before appending -', f2.read())

f1.close()
f2.close()

f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r')

f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print('content of first file after appending -', f1.read())
print('content of second file after appending -', f2.read())

f1.close()
f2.close()


# In[17]:


##Answer7:

fn = open('Giri3.txt', 'r')

fn1 = open('Giri5.txt', 'w')

cont = fn.readlines()
type(cont)
for i in range(0, len(cont)):
    if(i % 2!= 0):
        fn1.write(cont[i])
    else:
        pass

fn1.close()

fn1 = open('Giri5.txt', 'r')

cont1 = fn1.read()

print(cont1)

fn.close()
fn1.close()


# In[21]:


##Answer8:

data = data2 = ""

with open('Giri3.txt') as fp:
    data = fp.read()

with open('Giri5.txt') as fp:
    data2 = fp.read()

data += "\n"
data += data2
  
with open ('Giri7.txt', 'w') as fp:
    fp.write(data)


# In[22]:


##Answer9:

f = open('Giri5.txt', 'r')

lines = f.readlines()

f.close()

choice = 1
 
line = lines[choice].split()

Reversed = " ".join(line[::-1])

lines.pop(choice)
lines.insert(choice, Reversed)

u = open('Giri5.txt', 'w')
 
u.writelines(lines)
u.close()


# In[23]:


##Answer10:

f1 = open("Giri7.txt", "w")

with open("Giri5.txt", "r") as myfile:
    data = myfile.read()

data_1 = data[::-1]

f1.write(data_1)
  
f1.close()


# In[24]:


##Answer11:

class Stack:
      
    def __init__(self):

        self._arr = []

    def push(self, val):
        self._arr.append(val)
   
    def is_empty(self):

        return len(self._arr) == 0

    def pop(self):
          
        if self.is_empty():
            print("Stack is empty")
            return
          
        return self._arr.pop()

def reverse_file(filename):
       
    S = Stack()
    original = open(filename)
      
    for line in original:
        S.push(line.rstrip("\n"))
      
    original.close()
       
       
    output = open(filename, 'w')
      
    while not S.is_empty():
        output.write(S.pop()+"\n")
      
    output.close()

filename = "Giri5.txt"

reverse_file(filename)

with open(filename) as file:
        for f in file.readlines():
            print(f, end ="")


# In[ ]:




