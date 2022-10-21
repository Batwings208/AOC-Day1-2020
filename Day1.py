#Enjoy!
#part one
data =  open("path/Day1_files") #path of the puzzle input
result = data.readlines() # reading all the lines
lines = [int(item) for item in result] # separating each integer so they can be called easily

val = 0

for word in lines: # anything in lines
    for value in lines: # done again so it takes first integer and multiples it with every other one and when dones does the same with next int
        Sum = word + value # sum of answer
        if Sum == 2020 or Sum == "2020":
            print(f"sum: {Sum} \n Entry 1: {word} \n Entry 2: {value}") #checking
            print("Day 1-Part 1 Answer:", word * value) # answer
            break
        
        else:
            val += 1 # so when finished with the first one it moves on to the next int
            pass


 

#part two

val = 0
for word in lines:
    for value in lines:
        for val2 in lines: # done 3 times because we use 3 ints
            Sum = word + value + val2
            if Sum == 2020 or Sum == "2020":
                print(f"sum: {Sum} \n Entry 1: {word} \n Entry 2: {value} \n Entry 3: {val2}")
                print("Day 1-Part 2 Answer:", word * value * val2)
                break
            
            else:
                val += 1
                pass
