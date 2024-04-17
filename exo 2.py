def binary_to_gray(n):
    return n ^ (n >> 1)

def gray_to_binary(n):
    mask = n >> 1
    while mask != 0:
        n = n ^ mask
        mask = mask >> 1
    return n

def simplify_karnaugh_map(map):
    simplified = []
    num_vars = len(map)
    num_cells = len(map[0])
    for i in range(num_vars):
        simplified.append([])
        for j in range(num_cells):
            simplified[i].append('X')

    for i in range(num_vars):
        for j in range(num_cells):
            if map[i][j] == 1:
                simplified[i][j] = '1'
                for k in range(num_vars):
                    if k != i and map[k][j] == 1:
                        simplified[i][j] = '-'
                        break
                if simplified[i][j] == '1':
                    for k in range(num_cells):
                        if k != j and map[i][k] == 1:
                            simplified[i][j] = '-'
                            break

    return simplified

def print_karnaugh_map(map):
    for row in map:
        print("".join(row))

def karnaugh_minimization(expression):
    
    num_vars = expression.count('A') + expression.count('B') + expression.count('C') + expression.count('D')
    
    num_cells = 2 ** num_vars
    karnaugh_map = [[0 for _ in range(num_cells)] for _ in range(num_vars)]
    for i in range(num_cells):
        gray_code = binary_to_gray(i)
        for j in range(num_vars):
            karnaugh_map[j][i] = int(str(gray_code).zfill(num_vars)[j])
    
    for i in range(num_cells):
        binary_repr = str(bin(i))[2:].zfill(num_vars)
        value = eval(expression.replace('A', binary_repr[0])
                                 .replace('B', binary_repr[1])
                                 .replace('C', binary_repr[2])
                                 .replace('D', binary_repr[3]))
        karnaugh_map[num_vars - 1 - value][i] = 1
    
    simplified_map = simplify_karnaugh_map(karnaugh_map)
    
    print("Simplified Karnaugh Map:")
    print_karnaugh_map(simplified_map)

expression = "not A and (not B or C) or (A and B and C)"
karnaugh_minimization(expression)
