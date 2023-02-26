'''
for i in range(11): #0:10   lower < upper   1:50    
    print(i)


i = 0
while (i <= 10): #true  11 > false
    print(i)
    i +=1 #i = i+1
'''

'''
list1 = [10,9,8,7,6,5,4,3,2,1,0]
for elemnet in list1: #0:10   lower < upper   1:50    
    print(elemnet)


i = 10
while (i >= 0): #10 9 8 7 6 5 4 3 2 1 0 true -1 >false
    print(i)
    i -=1 #i = i-1
'''
'''
sum = 0
for i in range(1,11): #10   
    sum = sum + i   
  # 1 + 2 + 3 + 4 + ..... 10  = ?

print(sum) 
# 0 + 1 = 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
# 15 + 6 = 21 
# 21 + 7 = 28
# 28 + 8 = 36
# 36 + 9 = 45
#45 + 10 = 55

sum = 0
i= 1
while (i<=10):
    sum = sum + i 
    i += 1 # i = i +1 

print(sum)

sumEven =0 
sumOdd = 0
for i in range(1,11): #10      4%2 =0 even - 5%2 = 1 odd
    if (i % 2==0):
        sumEven = sumEven + i
    else:
        sumOdd = sumOdd + i
# 2 4 6 8 10 >> 30
# 1 3 5 7 9  >> 25
print(sumEven)
print(sumOdd)
'''

list1 = [15, 81, 5, 17, 20, 21, 13] 

for element in list1:  # 15%5 = 0 
    if(element %5 == 0): #true
         print(element)






