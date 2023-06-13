string = input() #take input
string2 = list(string.split(" ")) #split input
string3 = [] #list for int input
count = 0 #counter for divisors
for i in string2:
    i = int(i)
    string3.append(i) #int-ed input successfully
for j in range(string3[0],string3[1]+1): #count divisors
    if j%string3[2] == 0:
        count +=1 #counted successfully 
print(count)        #print number of divisors
