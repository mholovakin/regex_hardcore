# Course: Python Course
# Section: Functions
# Chapter: Function Scope
# Task Number: 1

try:
    value
except NameError:
    print("Variable \"value\" not defined", file=sys.stderr)
    sys.exit(0)

is_def = False
for line in user_code_lines:
    if re.search('\s*def\s*my_function\(\)\s*', line):
        is_def = True

if not is_def:
    print("Please, identify function", file=sys.stderr)
    sys.exit(0)

code_string = '\n'.join(user_code_lines)
is_global = False
if re.search('\s*global\s*value\s*.*\s*value\s*=\s*200\s*', code_string):
    is_global = True

if not is_global:
    print("Please, identify the error and fix it", file=sys.stderr)
    sys.exit(0)

is_prints = False
if re.search('\s*print\s*\(\s*my_function\s*\(\s*\)\).*\s*print\s*\(\s*value\)\s*', code_string):
    is_prints = True

if not is_prints:
    print("Please, print function and variable", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))