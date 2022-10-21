#part one
data =  open("/Users/godseye/Coding/PythonProjects/sideprojects/AdventOfCode/2020/Day1_files")
result = data.readlines()
lines = [int(item) for item in result]

val = 0
for word in lines:
    for value in lines:
        Sum = word + value
        if Sum == 2020 or Sum == "2020":
            print(f"sum: {Sum} \n Entry 1: {word} \n Entry 2: {value}")
            print("Day 1-Part 1 Answer:", word*value)
            break
        
        else:
            val += 1
            pass


 

#part two

val = 0
for word in lines:
    for value in lines:
        for val2 in lines:
            Sum = word + value + val2
            if Sum == 2020 or Sum == "2020":
                print(f"sum: {Sum} \n Entry 1: {word} \n Entry 2: {value} \n Entry 3: {val2}")
                print("Day 1-Part 2 Answer:", word*value*val2)
                break
            
            else:
                val += 1
                pass