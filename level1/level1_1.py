
def main():
    for i in range(5):
        f = open(f"level1_{i + 1}.in", "r")
        #f = open("level1_example.in", "r")
        lines = f.readlines()
        f.close()
        r = open(f"level1_{i + 1}.out", "w")
        for j, line in enumerate(lines):
            line.strip()
            #print(line)
            #print(j, line)
            if j > 0:
                r.writelines(winner(line) + "\n")
        r.close()


def winner(line):
    if line[0] == line[1]:
        #print(f"Tie! {line[0]}")
        return line[0]
    else:
        if "R" in line and "P" in line:
            #print("Paper wins against rock!")
            return "P"
        elif "R" in line and "S" in line:
            #print("Rock wins against scissor!")
            return "R"
        elif "S" in line and "P" in line:
            #print("Stone wins against Paper!")
            return "S"


if __name__ == "__main__":
    main()

