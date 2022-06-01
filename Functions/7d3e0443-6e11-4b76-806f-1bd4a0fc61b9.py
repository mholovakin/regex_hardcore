# Course: Python Course
# Section: Functions
# Chapter: Function Creation
# Task Number: 1

is_print = False
for line in user_print_lines:
    if re.search('\s*Hello\s*(W|w)orld\s*', line):
        is_print = True

if not is_print:
    print("Please, print the line, which is indicated in the task", file=sys.stderr)
    sys.exit(0)

is_def = False
for line in user_code_lines:
    if re.search('\s*def\s*hello_world\(\s*\)\s*', line):
        is_def = True

if not is_def:
    print("Please, identify function \"hello_world()\"", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))