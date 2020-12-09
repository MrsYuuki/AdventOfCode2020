def open_file(file_name):
    file = open(file_name, "r")
    file_lines = []
    line = file.readline()
    while line!="":
      n_line = line.replace("\n", "")
      file_lines.append(int(n_line))
      line = file.readline()
    return file_lines



numbers = open_file("Advent1.txt")
numbers.sort()

def find2_2020(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == 2020:
                return [numbers[i], numbers[j], numbers[i]*numbers[j]]

def find3_2020(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    return [numbers[i], numbers[j], numbers[k], numbers[i]*numbers[j]*numbers[k]]

print(find3_2020(numbers))

