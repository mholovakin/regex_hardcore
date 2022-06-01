# Course: Python Course
# Section: Errors and Exceptions
# Chapter: Handling Exceptions
# Task Number: 1


code_string = '\n'.join(user_code_lines)
if not re.search("\s*try\s*:.*\s*def\s*func\s*\(\s*\)\s*:.*\s*print\s*\((\"|\')The\s*num\s*entered\s*is\s*:\s*(\"|\')\s*,\s*x\)\s*.*\s*func\s*\(\d+\)\s*", code_string):
    print('Pleease, use \"try\" statement to check your function', file=sys.stderr)
    sys.exit(0)

if not re.search('\s*except\s*:.*\s*print\s*\((\"|\')(a|A)n\s*error\s*has\s*occured(\"|\')\s*\)\s*', code_string):
    print("Please, use \"catch\" statement to catch error", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if re.search('\s*(A|a)n\s*error\s*has\s*occurred\s*', line):
        is_print = True

if not is_print:
    print("Please print \"An error has occured\" in catch block", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))