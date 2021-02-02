words = []
file = open("problem42.txt", "r")
file1 = file.read().replace(",", " ")
file1 = file1.replace('"', "")
words = file1.split()
file.close()
#the longest string has 14 charachters >> max triange number <=14x24
i = 1
triangles = []
#nem kell 100ig
for i in range(1, 100):
    triangles.append(i*(i+1)/2)
def decide_tri(word):
    sum = 0
    for x in word:
        sum = sum + ord(x) - 64
    if sum in triangles:
        return True
    else:
        return False
d = 0
for x in words:
    if decide_tri(x) == True:
        d+=1
    else:
        continue
print(d)
