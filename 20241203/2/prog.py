import math
import sys

def to_float(x):
    try:
        return float(x)
    except ValueError:
        return 0.0

OP_commands = ['add', 'sub', 'div', 'mul']
CMP_commands = ['ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle']
#                ==      !=      >       >=       <      <=  

labels = {}
commands = []
variables = {}
def interpret(program):
    lines = program.splitlines()
    count = 0
    for j in range(len(lines)):
        line = lines[j].split()
        if line and line[0].endswith(':'):
            labels[line[0][:-1]] = count
            line = line[1:]
        commands.append(line)
        count += 1

    i = 0
    while i < count:
        match commands[i]:
            case ['stop']:
                return
            case ['store', num, var]:
                variables[var] = to_float(num)
            case [op, source, oper, var] if op in OP_commands:
                try:
                    variables.setdefault(source, 0)
                    variables.setdefault(oper, 0)
                    variables.setdefault(var, 0)
                    if op == 'add':
                        variables[var] = variables[source] + variables[oper]
                    if op == 'sub':
                        variables[var] = variables[source] - variables[oper]
                    if op == 'div':
                        variables[var] = variables[source] / variables[oper]
                    if op == 'mul':
                        variables[var] = variables[source] * variables[oper]
                except Exception:
                    variables[var] = math.inf
            
            case [cmp, source, oper, metka] if cmp in CMP_commands:
                if metka not in labels:
                    break
                variables.setdefault(source, 0)
                variables.setdefault(oper, 0)

                if cmp == 'ifeq':
                    if variables[source] == variables[oper]:
                        i = labels[metka]
                        continue
                elif cmp == 'ifne':
                    if variables[source] != variables[oper]:
                        i = labels[metka]
                        continue
                elif cmp == 'ifgt':
                    if variables[source] > variables[oper]:
                        i = labels[metka]
                        continue
                elif cmp == 'ifge':
                    if variables[source] >= variables[oper]:
                        i = labels[metka]
                        continue
                elif cmp == 'iflt':
                    if variables[source] < variables[oper]:
                        i = labels[metka]
                        continue
                elif cmp == 'ifLe':
                    if variables[source] <= variables[oper]:
                        i = labels[metka]
                        continue
            case ['out', var]:
                print(variables[var])
        i += 1


s = sys.stdin.read()
interpret(s)