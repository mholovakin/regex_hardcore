# Course: Python Course
# Section: Functions
# Chapter: Function Scope
# Task Number: 2

try:
    var
except NameError:
    print("Variable \"var\" not defined", file=sys.stderr)
    sys.exit(0)

is_def = False
for line in user_code_lines:
    if re.search('\s*def\s*var_val\s*\(\s*\)\s*', line):
        is_def = True

if not is_def:
    print("Please, identify function", file=sys.stderr)
    sys.exit(0)

code_string = '\n'.join(user_code_lines)

if not re.search('\s*var\s*=\s*5', code_string):
    print("Please, don\'t change initial variable value", file=sys.stderr)
    sys.exit(0)

is_global = False
if re.search('\s*global\s*var\s*.*var\s*\=\s*15\s*', code_string):
    is_global = True

if not is_global:
    print("Please, make the variable global and than change the value", file=sys.stderr)
    sys.exit(0)

if not re.search('\s*var_val\s*\(\s*\)\s*', code_string):
    print("Please, call the function", file=sys.stderr)
    sys.exit(0)

if not ('5' in user_print_lines and '15' in user_print_lines):
    print("Please, print the values of variables", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))