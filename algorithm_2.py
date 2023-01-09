#Consider the input.txt file location same as that of the algorithm_2.py file

matching_cast0_len = 0
matching_cast1_len = 0
counter=0
tempCast={}
casts=[]

with open("input.txt") as f:
    number_of_casts = str(f.readline())[2:-4]                              #  Reading number of casts
    n=int(number_of_casts)
    
    line=[]
    for i in range(n):
        line=str(f.readline()[11:-2]).split(',')                     # Reading each line separated by ,
        for w in range(len(line)):
            line[w]=line[w][line[w].find('“')+1:line[w].find('”')]     # Reading each cast name without ""
        casts.append(set(line))

if n > 2:
    z=casts[0].intersection(casts[1])                           # z variable is ised to store matching cast between cast[0] and cast[1]
    for i in range(2,n):
        matching_cast0 = casts[0].intersection(casts[i])           # intersection() function used to find  casts between cast[0] and cast[i]
        matching_cast0_len = len(matching_cast0)                   #  the number of matching casts
        matching_cast1 = casts[1].intersection(casts[i])          # intersection() function used to find common casts between cast[1] and cast[i]
        matching_cast1_len = len(matching_cast1)
        if matching_cast0_len==1 and matching_cast1_len == 1:
            counter = counter+1
            if counter > 1:
                break
                    
            tempCast=casts[i]
            

    if len(z)==1:
            print("shortest connection =1, cast = ", z)      
    elif counter > 2 or counter == 0:
        print("Shortest connection > 2 or there is no connection.")
    else:
        print("shortest connection=2, ",tempCast)

else:
    print("n has to be greater than 2")
    
    


