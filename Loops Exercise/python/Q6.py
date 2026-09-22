data =[10,20,30,40,50]
total = 0
for i in range (len(data)):
    if i % 2 == 1:
        total += data[i]
print(total)        