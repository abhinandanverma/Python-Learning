# Exercise 8. Count occurrences of a specific element in a list
list =[10,20,10,30,10,40,50]
target = 10
count=0
for i in list:
    if i ==target:
        count+=1

print(target,"appears ", count, "times")