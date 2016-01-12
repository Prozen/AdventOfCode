instructions = """jio a, +22
inc a
tpl a
tpl a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jmp +19
tpl a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7""".splitlines()
instructions = [x.split() for x in instructions]
state = {'a':1,'b':0}
current  = 0
while current < len(instructions) and current > -1:
    if instructions[current][0] == 'inc':
        state[instructions[current][1]]+=1
        current+=1
    elif instructions[current][0] == 'hlf':
        state[instructions[current][1]]/=2
        current+=1
    elif instructions[current][0] == 'tpl':
        state[instructions[current][1]]*=3
        current+=1
    elif instructions[current][0] == 'jmp':
        current+=int(instructions[current][1])
    elif instructions[current][0] == 'jie':
        if state[instructions[current][1][0]] %2 == 0:
            current+=int(instructions[current][2])
        else: current+=1
    elif instructions[current][0] == 'jio':
        if state[instructions[current][1][0]] == 1:
            current+=int(instructions[current][2])
        else: current+=1
print(state)
