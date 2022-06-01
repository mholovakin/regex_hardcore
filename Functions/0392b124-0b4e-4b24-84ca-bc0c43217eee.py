# Course: Python Course
# Section: Functions
# Chapter: What are Functions
# Task Number: 1

is_def = False
for line in user_code_lines:
    if re.search('\s*def\s*(W|w)elcome\s*\(\s*\)\s*', line):
        is_def = True

if not is_def:
    print("Please, identify function \"welcome()\"", file=sys.stderr)
    sys.exit(0)


is_print = False
for line in user_print_lines:
    if re.search('\s*(W|w)elcome\s*to\s*the\s*world\s*of\s*(P|p)rogramming\s*', line):
        is_print = True

if not is_print:
    print("Please, print the line, which is indicated in the task", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))