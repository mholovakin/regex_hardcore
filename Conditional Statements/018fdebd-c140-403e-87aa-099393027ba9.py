# Course: Python Course
# Section: Conditional Statements
# Chapter: The Break and Continue Statements
# Task Number: 2

try:
    numbers
except NameError:
    print("Variable \"numbers\" not defined", file=sys.stderr)
    sys.exit(0)

if not numbers == [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]:
    print("Please, use provided initial values of variables", file=sys.stderr)
    sys.exit(0)


is_for = False
for line in user_code_lines:
    if re.search('\s*for\s*[a-z]+\s*in\s*numbers\s*', line):
        is_for = True

if not is_for:
    print("Please, code \"for\" statement through array", file=sys.stderr)
    sys.exit(0)

is_div = False
for line in user_code_lines:
    if re.search('\s*number\s*\%\s*5\s*\=\=\s*0\s*', line):
        if_div = True

if not is_div:
    print("Please, print numbers, that divisible by 5", file=sys.stderr)
    sys.exit(0)

is_break = False
for line in user_code_lines:
    if re.search('\s*[a-z]+\s*>=\s*150(\)|):\s*break\s*', line):
        is_break = True

if not is_break:
    print("Please, use \"break\" statement in your code", file=sys.stderr)
    sys.exit(0)

if not ('15' in user_print_lines and '55' in user_print_lines and '75' in user_print_lines):
    print("Wrong answer. Please, check \"break-continue\" operators", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))