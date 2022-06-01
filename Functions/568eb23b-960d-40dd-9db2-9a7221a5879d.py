# Course: Python Course
# Section: Functions
# Chapter: Functions as Arguments
# Task Number: 1



code_string = '\n'.join(user_code_lines)

is_func_1 = False
if re.search('\s*def\s*func_1\(\):\s*.*print\((\"|\')I\s*am\s*inside\s*another\s*function\s*(\"|\')\)', code_string):
    is_func_1 = True

if not is_func_1:
    print("Please, create a function named func_1, where you print \'I am inside another function\'", file=sys.stderr)
    sys.exit(0)

is_func = False
if re.search('\s*def\s*func\(\):\s*.*func_1\(\)', code_string):
    is_func = True

if not is_func:
    print("Please, create a function named func, where you call func_1", file=sys.stderr)
    sys.exit(0)


is_print = False
for line in user_print_lines:
    if re.search('(I|i)\s*am\s*inside\s*another\s*function\s*', line):
        is_print = True

if not is_print:
    print("Please, print the line, which is indicated in the task", file=sys.stderr)
    sys.exit(0)

passed = False
if re.search('\s*func\s*\(\s*\)\s*', code_string):
    passed = True

if not passed:
    print("Please, call the function func()", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))