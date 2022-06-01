# Course: Python Course
# Section: Functions
# Chapter: What are Functions
# Task Number: 2

is_print = False
for line in user_print_lines:
    if re.search('\s*Hello,\s*I\s*am\s*learning\s*Python\s*.\s*', line):
        is_print = True

if not is_print:
    print("Please, print the line, which is indicated in the task", file=sys.stderr)
    sys.exit(0)

is_def = False
for line in user_code_lines:
    if re.search('\s*def\s*my_function\s*\(\s*\)\s*', line):
        is_def = True

if not is_def:
    print("Please, identify function \"my_function()\"", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))