def read(filename):
    with open(filename, "r") as f:
        side = int(f.readline()[:-1])
        map = [[0 for  in range(side)] for  in range(side)]
        for i in range(side):
            line = f.readline()[:-1]
            for j in range(side):
                map[i][j] = line[j]
        outputs = []
        input = int(f.readline()[:-1])
        for i in range(input):
            line = f.readline()[:-1]
            line = line.split(",")
            line = [int(x) for x in line]
            outputs.append(map[line[1]][line[0]])

    return outputs
def write_to_file(
print(read("level1_example.in"))
print(read("level1_1.in"))
print(read("level1_2.in"))
print(read("level1_3.in"))
print(read("level1_4.in"))
print(read("level1_5.in"))
