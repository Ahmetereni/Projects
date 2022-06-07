
def funky(list):
    y = 0
    x = 0
    z = 0
    for i in range(len(list)):

        if list[i][-1] == "y":
            y += int(list[i][:-1])

        elif list[i][-1] == "x":
            x += int(list[i][:-1])

        else:
            z += int(list[i])
    return [y, x, z]
