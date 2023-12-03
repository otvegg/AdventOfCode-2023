sum = 0
with open('.\Day1\input.txt','r') as f:
    for line in f.readlines():
        numbers = []
        for i in line:
            if i.isnumeric():
                numbers.append(i)

        sum += int(numbers[0]+ numbers[-1])

print(sum)
