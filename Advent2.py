def open_file(file_name):
    interval = []
    letter_table = []
    password_table = []
    file = open(file_name, "r")
    line = file.readline()
    while line!="":
        n_line = line.replace("\n", "")
        n_line = n_line.split()
        intervals = (n_line[0].split("-"))
        interval.append(intervals)
        letter_table.append(n_line[1][0])
        password_table.append(n_line[2])
        line = file.readline()

    return interval, letter_table, password_table

def password_check(interval, letters, passwords):
    good_passwords = 0
    for number in range(len(letters)):
        if_good = 0
        for i in range(len(passwords[number])):
            if passwords[number][i] == letters[number]:
                if_good += 1
        if len(interval[number]) == 2:
            if if_good >= int(interval[number][0]) and if_good <= int(interval[number][1]):
                good_passwords += 1
        else:
            if if_good == int(interval[number][0]):
                good_passwords += 1
    return good_passwords

def password_check2(interval, letters, passwords):
    good_passwords = 0
    for number in range(len(interval)):
        if_good = 0
        for i in interval[number]:
            i = int(i) - 1
            if passwords[number][i] == letters[number]:
                if_good += 1
        if if_good == 1:
            good_passwords += 1
    return good_passwords

interval, letter_table, password_table = open_file("Advent2.txt")
print(password_check(interval, letter_table, password_table))
print(password_check2(interval, letter_table, password_table))


