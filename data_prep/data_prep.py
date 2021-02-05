def read_grid(file, data_type=chr):
    data = file.read().split('\n')
    for i in range(len(data)):
        data[i] = list(data[i])
        for j in range(len(data[i])):
            data[i][j] = data_type(data[i][j])
    return data

def read_lines(file, data_type=int, split_char=' '):
    data = file.read().split('\n')
    for i in range(len(data)):
        data[i] = data.split(split_char)
        if len(data[i]) == 1:
            data[i] = data_type(data[i][0])
            continue
        for j in range(len(data[i])):
            data[i][j] = data_type(data[i][j])
    return data