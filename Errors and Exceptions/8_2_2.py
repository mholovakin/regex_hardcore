# Course: Python Course
# Section: Errors and Exceptions
# Chapter: Handling Exceptions
# Task Number: 2


is_func = False
for line in user_code_lines:
    if re.search('\s*def\s*func\s*\(\s*a\s*,\s*b\s*\)\s*:', line):
        is_func = True

if not is_func:
    print('Please, define the function', file=sys.stderr)
    sys.exit(0)


code_string = '\n'.join(user_code_lines)
if not re.search('\s*try\s*:.*\s*print\s*\(\s*a\s*\+\s*b\s*\)\s*.*\s*except\s*:.*\s*print\s*\(\s*(\"|\')(A|a)n\s*error\s*has\s*occured(\"|\')\s*\).*\s*finally\s*:.*\s*print\s*\((\"|\')(E|e)xecution\s*has\s*stopped(\'|\")\)\s*', code_string):
    print("Please, use \"try-except-finally\" statements as defined in task", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if re.search('\s*(E|e)xecution\s*has\s*stopped\s*', line):
        is_print = True

if not is_print:
    print("Please, call the function", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))