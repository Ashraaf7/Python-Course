'''
list1 = ['Ahmed','Ali','Noor','Ashraf' ,'Tarek'] #1D
           #0       #1   2       3          4
#'Ahmed' >> A h m e d
print(list1[2]) #Noor
for element in list1:
    for chara in element:
        print(chara)

#element >> Ahmed    chara >> A h m e d 
#element >> Ali      chara >> A l i
#element >> Noor     chara >> N o o r
#.....
'''

list2 = [
    #0 1 2
    [1,2,3],  #0
    [4,5,6],  #1        #2D
    [7,8,9]   #2
]
for row in list2:
    for col in row:
      print(col)
#row > [1,2,3]    col>> 1 2 3
#row > [4,5,6]    col > 4 5 6
#row > [7,8,9]    col > 7 8 9
#1
#2
#3
#4
#5
#6
#7
#8
#9
