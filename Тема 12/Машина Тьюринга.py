def MT(program, line, state, cell):
    while True:
        row = program[state]
        col = row[line[cell]]
        if not col:
            break
        # col[0] - символ, на который заменяется текущий
        line[cell] = col[0]
        if col[1] == 0:
            break
        cell += col[1]
        state = col[2]
    return line

"""
-1 - L
1  - R
0  - S
"""

program = {'q0' : {'l': ('l', -1, 'q1'), '0': None, '1': None},
           'q1' : {'l': ('l', 0, 'q1'), '0': ('1', -1, 'q1'), '1': ('0', 0, 'q1')}}
