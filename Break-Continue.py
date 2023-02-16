list1 = ['Ahmed','Mohamed','Ashraf','Ali','Noor']

for element in list1:
    if(element=='Ashraf'):
        #break
        continue
    else:
        print(element)
#Break
# element > Ahmed >> Ahmed
#element > Mohamed >> Mohamed
#element > Ashraf  

#continue
# element > Ahmed >> Ahmed
#element > Mohamed >> Mohamed
#element > Ashraf 
# element > Ali >>  Ali
#element > Noor >>  Noor