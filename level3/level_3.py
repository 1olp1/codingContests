level = 3
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
            if j > 0:
                n_r, n_p, n_s = get_inp(line)
                matchups = find_matchups(n_r, n_p, n_s)
                r.writelines(str(matchups) + "\n")
        r.close()


def get_inp(line):
    n_r = int(line[:line.find("R")])
    n_p = int(line[line.find("R") + 1:line.find("P")])
    n_s = int(line[line.find("P") + 1:line.find("S")])
    return n_r, n_p, n_s


def find_matchups(n_r, n_p, n_s):
    matchups = n_r * "R" + n_p * "P" + n_s * "S"
    matchups_list = make_list(matchups)
    #print("Initial: ", matchups_list)
    r_left = fs_after_n_rounds(matchups, "R", 2)
    #print(f"R left: {r_left}")
    if r_left == 0:
        return make_string_from_list(matchups_list)

    n_p_left = n_p

    for i in range(0, len(matchups), 4):
        if make_string_from_list(matchups_list)[i:i + 4] == "RRRR":
            if n_p_left > 0:
                matchups_list[i:i + 4] = "RRRP"
                matchups_list[n_r + n_p - n_p_left] = "R"
                n_p_left -= 1
                #print("New matchups:", matchups_list)
                r_left = fs_after_n_rounds(make_string_from_list(matchups_list), "R", 2)
                #print("R left: ", r_left, "\n")
                if r_left == 0:
                    return make_string_from_list(matchups_list)

    if r_left > 0:
        for i in range(0, len(matchups), 2):
            if make_string_from_list(matchups_list)[i:i + 2] == "PS" and n_p_left == 1:
                matchups_list[i - 1:i + 1] = "PR"
                #print("New matchups:", matchups_list)
                r_left = fs_after_n_rounds(make_string_from_list(matchups_list), "R", 2)
                #print("R left: ", r_left, "\n")
                if r_left == 0:
                    return make_string_from_list(matchups_list)


def make_string_from_list(in_list):
    new_str = ""
    for letter in in_list:
        new_str += letter
    return new_str


def make_list(matchups_str):
    list_str = []
    for letter in matchups_str:
        list_str.append(letter)
    return list_str


def fs_after_n_rounds(matchups, fstyle, n_rounds):
    fs_left = 0
    #one_round = winners_mult_rounds(matchups, 1)
    two_rounds = winners_mult_rounds(matchups, n_rounds)
    #print(matchups)
    #print("after one round: ", one_round)
    #print("after two rounds: ", two_rounds)

    for letter in two_rounds:
        if fstyle in letter:
            fs_left += 1

    return fs_left


def winners_mult_rounds(w_last_round, rounds):
    w_current = w_last_round
    for i in range(rounds):
        w_current = round_winners(w_current)
    return w_current


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
