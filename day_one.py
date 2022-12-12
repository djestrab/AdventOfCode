

def parse_input(filename: str) -> list:
    """
    Take filename as input and return parsed in a list
    """

    parsed_input = []
    with open(filename) as file:
        temp_list = []
        for line in file:
            if line != "\n":
                temp_list.append(int(line.strip()))
            else:
                parsed_input.append(temp_list)
                temp_list = []
        parsed_input.append(temp_list)
    return parsed_input


# Day 1
def open_day_one():
    input_list = parse_input("inputs/1.txt")
    sums = [sum(elf) for elf in input_list]
    return max(sums)


def open_day_one_part_two():
    input_list = parse_input("inputs/1.txt")
    sums = [sum(elf) for elf in input_list]
    sums.sort(reverse=True)
    return sum(sums[:3])


print(open_day_one())
print(open_day_one_part_two())

