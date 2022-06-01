# Course: Python Course
# Section: Errors and Exceptions
# Chapter: Syntax Errors Exceptions
# Task Number: 2

try:
    alpha
except NameError:
    print("Variable \"alpha\" not defined", file=sys.stderr)
    sys.exit(0)

if alpha != 4:
    print("Please, use provided initial value of variable", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if re.search("\s*Done\s*", line):
        is_print = True


if not is_print:
    print("Please, print \"Done\" in \"if\" statement", file=sys.stderr)
    sys.exit(0)

code_string = '\n'.join(user_code_lines)
if not re.search('\s*if\s*\(\s*alpha\s*>=\s*4\s*\)\s*:.*\s*print\s*\((\"|\')Done(\'|\")\s*\)\s*', code_string):
    print("Please, correct the mistake in the code", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))