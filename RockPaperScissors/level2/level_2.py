level = 2
no_rounds = 2


def main():
    for i in range(5):
        f = open(f"level{level}_{i + 1}.in", "r")
        #f = open(f"level{level}_example.in", "r")
        lines = f.readlines()
        f.close()
        r = open(f"level{level}_{i + 1}.out", "w")
        for j, line in enumerate(lines):
            line.strip()
            # print(line)
            # print(j, line)
            if j > 0:
                winners_two_rounds = winners_mult_rounds(line, no_rounds)
                r.writelines(winners_two_rounds + "\n")
        r.close()


def winners_mult_rounds(w_last_round, no_rounds):
    w = w_last_round
    for i in range(no_rounds):
        w = round_winners(w)
    return w


def round_winners(line):
    winners = ""
    for i in range(0, len(line) - 1, 2):
        winners = winners + winner(line[i] + line[i + 1])
    return winners


def winner(line):
    if line[0] == line[1]:
        # print(f"Tie! {line[0]}")
        return line[0]
    else:
        if "R" in line and "P" in line:
            # print("Paper wins against rock!")
            return "P"
        elif "R" in line and "S" in line:
            # print("Rock wins against scissor!")
            return "R"
        elif "S" in line and "P" in line:
            # print("Stone wins against Paper!")
            return "S"


if __name__ == "__main__":
    main()

