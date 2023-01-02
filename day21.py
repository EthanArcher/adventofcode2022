from aoc import read_input


def operate(v1: int, operator, v2: int):
    match operator:
        case "+":
            return str(v1 + v2)
        case "-":
            return str(v1 - v2)
        case "*":
            return str(v1 * v2)
        case "/":
            return str(v1 // v2)


def reverse_equation(value, right):
    global values
    equation = values.get(value)
    if value == "humn":
        print(right)
        return right
    if equation[0].isnumeric():
        if equation[1] == "+":
            reverse_equation(equation[2], right - int(equation[0]))
        elif equation[1] == "-":
            reverse_equation(equation[2], int(equation[0]) - right)
        elif equation[1] == "*":
            reverse_equation(equation[2], right / int(equation[0]))
        elif equation[1] == "/":
            reverse_equation(equation[2], int(equation[0]) / right)
    else:
        if equation[1] == "+":
            reverse_equation(equation[0], right - int(equation[2]))
        elif equation[1] == "-":
            reverse_equation(equation[0], right + int(equation[2]))
        elif equation[1] == "*":
            reverse_equation(equation[0], right / int(equation[2]))
        elif equation[1] == "/":
            reverse_equation(equation[0], right * int(equation[2]))


if __name__ == "__main__":
    lines = read_input("day21", str)
    values = {}

    for line in lines:
        split = line.split(" ")
        v = split[0][:-1]
        equation = list()
        equation.append(split[1])

        if len(split) > 2:
            equation.append(split[2])
            equation.append(split[3])

        values.update({v: equation})

    still_calculating = True

    for i in range(50):

        still_calculating = False

        # fill in any numbers we have
        for v in values:
            equation = values.get(v)
            if len(equation) > 1 and not v == "humn":
                still_calculating = True
                new_equation = list()
                if not equation[0].isnumeric() and len(values.get(equation[0])) == 1:
                    new_equation.append(values.get(equation[0])[0])
                else:
                    new_equation.append(equation[0])
                new_equation.append(equation[1])
                if not equation[2].isnumeric() and len(values.get(equation[2])) == 1:
                    new_equation.append(values.get(equation[2])[0])
                else:
                    new_equation.append(equation[2])
                values.update({v: new_equation})

        # if they are both numbers now do the calculation
        for v in values:
            equation = values.get(v)
            if len(equation) == 3 and equation[0].isnumeric() and equation[2].isnumeric():
                values.update({v: [operate(int(equation[0]), equation[1], int(equation[2]))]})

    for v in values:
        print(v, values.get(v))

    reverse_equation(values.get("root")[0], int(values.get("root")[2]))
