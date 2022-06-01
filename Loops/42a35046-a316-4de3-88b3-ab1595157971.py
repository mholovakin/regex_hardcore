# Course: Python Course
# Section: Loops
# Chapter: What are Loops
# Task Number: 3

try:
    animals
except NameError:
    print("Variable \"animals\" not defined", file=sys.stderr)
    sys.exit(0)

if not (animals == ('lion', 'cat', 'dog', 'crocodile', 'monkey')):
    print("Please, use provided initial value of variable", file=sys.stderr)
    sys.exit(0)

var_1 = ''
if_line = ''
is_for = False
is_continue = False
for line in user_code_lines:
    if re.search('for', line):
        var_1 = line
        is_for = True
    if re.search('if', line):
        if_line = line
    if re.search('\s*continue\s*', line):
        is_continue = True


if not is_for:
    print("Please, use \"for loop\"", file=sys.stderr)
    sys.exit(0)

if not is_continue:
    print("Please, use \"continue\"", file=sys.stderr)
    sys.exit(0)

first = var_1.index('for'[-1])
second = var_1.index('in')
variable = var_1[first+1:second]
variable = variable.strip()

if not re.search('\s*for\s*{}\s*in\s*animals\s*'.format(variable), var_1):
    print("Please, loop through \"language\" variable", file=sys.stderr)
    sys.exit(0)

if not re.search('\s*if\s*{}\s*\=\=\s*(\'|\")dog(\'|\")\s*'.format(variable), if_line):
    print("Error. Please, check your code in \"if\" statement", file=sys.stderr)
    sys.exit(0)

if not ('lion' in user_print_lines and 'cat' in user_print_lines and 'crocodile' in user_print_lines and 'monkey' in user_print_lines):
    print('Please, print all animals except dog', file=sys.stderr)
    sys.exit(0)

if 'dog' in user_print_lines:
    print('Plese, print all animals except dog', file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))