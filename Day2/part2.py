sum = 0
criteria = {"red": 12, "green": 13, "blue": 14}

with open(".\Day2\input.txt", "r") as f:
    for line in f.readlines():
        id = int(line.split(":")[0].split(" ")[1])
        sets = line.split(":")[1].split(";")

        bag = {"red": 0, "green": 0, "blue": 0}
        possible = True
        for set in sets:
            colours = set.split(",")
            for colour in colours:
                count, colour = colour.strip().split(" ")
                bag[colour] = max(bag.get(colour, 0), int(count))

        
        sum += bag['red']*bag['blue']*bag['green']

print(sum)
