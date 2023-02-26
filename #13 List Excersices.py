'''
list1 = [1,2,3,4,5]
print(list1[0])
print(list1[4]) #1
print(list1[-1]) #2
print(list1[3])
'''
'''
list2 = [1,2]   
list2.append(3) #[1,2,3]
list2.append(4) #[1,2,3,4]
print(list2)
list2.remove(1)  #[2,3,4]
list2.remove(2)  #[3,4]
print(list2)
'''
'''
list3 = [1,2,3]
list4 = [4,5,6,7]
mergedList = list3 + list4
print(mergedList)
'''
'''
list5 = [5,4,6,8,1,0]
list5.sort() #[0,1,4,5,6,8]
print(list5)
count =len(list5)
print(count)
'''

list6 = ['Ahmed', 'Ashraf' , 'Mohamed' , ['Ali','Hany','Fareed'] ]
# Ali Fareed 
print(list6[3][0] + " " + list6[3][2])