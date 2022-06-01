# Course: Python Course
# Section: Loops
# Chapter: While Loops
# Task Number: 2

is_var = False
var_1 = ''
for line in user_code_lines:
    if re.search('\s*\=\s*5\s*', line):
        var_1 = line
        is_var = True
        break

if not is_var:
    print("Variable not defined (value 5)", file=sys.stderr)
    sys.exit(0)


second = var_1.index('=')
variable_1 = var_1[:second]
variable_1 = variable_1.strip()

is_while = False
is_print = False
is_minus = False
for line in user_code_lines:
    if re.search('\s*while\s*\(\s*{}\s*>=\s*2\s*\)\s*'.format(variable_1), line):
        is_while = True
    if re.search('\s*print\s*\(\s*{}\s*\)'.format(variable_1), line):
        is_print = True
    if re.search('\s*{}\s*(-=|\s*=\s*{}\s*-\s*)\s*1'.format(variable_1, variable_1), line):
        is_minus = True

if not is_while:
    print("Please, use while and compare your variable with 2", file=sys.stderr)
    sys.exit(0)

if not is_print:
    print("Please, print your variable on each iteration", file=sys.stderr)
    sys.exit(0)

if not is_minus:
    print("Please, decrease the value of your variable at each iteration of the loop", file=sys.stderr)
    sys.exit(0)

code_string = '\n'.join(user_code_lines)

if not re.search('\s*else.*\s*print\s*\(\s*(\"|\')Done(\"|\')\s*\)', code_string):
    print("Please, print \"Done\" in else statement", file=sys.stderr)
    sys.exit(0)

if user_print_lines != ['5','4','3','2','Done']:
    print("Wrong output. Please, find mistake and try again", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))