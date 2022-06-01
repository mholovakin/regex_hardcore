# Course: Python Course
# Section: Errors and Exceptions
# Chapter: User Defined Exceptions
# Task Number: 1

try:
    var
except NameError:
    print("Variable \"var\" not defined", file=sys.stderr)
    sys.exit(0)

var_1 = ''
for line in user_code_lines:
    if re.search('class', line):
        var_1 = line

if var_1 == '':
    print("Class with user exception not defined", file=sys.stderr)
    sys.exit(0)

first = var_1.index('class'[-1])
second = var_1.index('(')
variable = var_1[first+2:second]
variable = variable.strip()

is_print = False
for line in user_code_lines:
    if re.search('\s*print\s*\((\"|\')Error!!!\s*Var\s*is\s*greater\s*than\s*5(\'|\")\s*\)\s*', line):
        is_print = True

if not is_print:
    print("Please, print \"Error!!! Var is greater than 5\" in your exception", file=sys.stderr)
    sys.exit(0)


if not re.search('\s*try\s*:.*\s*if\s*var\s*<\s*5\s*:.*\s*print\s*\(\s*var\s*\).*\s*except\s*{}\s*:\s*'.format(variable), code_string):
    print("Please, compare variable \"var\" with 5 in \"try\" clause and use \"except\" with your exception class", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))