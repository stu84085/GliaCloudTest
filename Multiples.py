'''
Created on 2019年1月28日

@author: daton
'''
numbers =[]

count = 0

while True :
    count += 1 #只列前三top
    #print(count)
    if count >= 1000:
        break
    
    if count % 3==0 or count % 5==0:
            numbers.append(count)
    
summary=0

for num in numbers:
    print(num)
    summary +=num;
    
print("sum is ",summary)