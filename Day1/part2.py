wnumbers = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


def answer():
    sum = 0
    with open(".\Day1\input.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()

            first, last = None, None
            endc = True
            c = 1
            bres = ""
            while endc:
                if c == len(line):
                    if first == None:
                        first = last
                    elif last == None:
                        last = first
                    endc = False

                if first and last:
                    endc = False
                bres = line[-c] + bres
                if not first and not line[0:c].isalpha():
                    first = line[c - 1]

                if not last and not bres.isalpha():
                    last = bres[0]

                for key, value in wnumbers.items():
                    if not first and value in line[0:c]:
                        first = key

                    if not last and value in bres:
                        last = key

                c += 1

            first = str(first)
            last = str(last)
            sum += int(first + last)
    return sum


result = answer()
correct = 56017

if result != correct:
    print(f"Answer is incorrect. Correct is {correct}, your answer is {result}")
else:
    print(f"Your solution gave the correct answer: {result}")
