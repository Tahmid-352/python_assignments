myString = str(input('Enter any name: '))
letter = str(input("Enter a letter :"))
myList = []
for i in myString:
    myList.append(i)
count = 0
for i in myList:
    if i == letter:
        count = count + 1
    else:
        continue
print (count)