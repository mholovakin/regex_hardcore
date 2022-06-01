# Course: Python Course
# Section: Loops
# Chapter: For Loops
# Task Number: 3

try:
    total
except NameError:
    print('Variable \"total\" not defined', file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if line == '120':
        is_print = True

if not is_print:
    print("Wrong value or empty print", file=sys.stderr)
    sys.exit(0)

var_1 = 0
for line in user_code_lines:
    if re.search('for', line):
        var_1 = line

first = var_1.index('for'[-1])
second = var_1.index('in')
variable = var_1[first+1:second]
variable = variable.strip()

code_string = '\n'.join(user_code_lines)

if not re.search("\s*for\s*{}\s*in\s*range\(\s*1\s*,\s*16\s*\)".format(variable), code_string):
    print("Please, code for loop in range between 1 and 16", file=sys.stderr)
    sys.exit(0)

if not re.search('\s*total\s*(\+\=|\=\s*total\s*\+)\s*{}\s*'.format(variable), code_string):
    print("Please, add integer to \"total\" variable", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))