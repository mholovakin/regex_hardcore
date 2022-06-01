# Course: Python Course
# Section: Conditional Statements
# Chapter: The if, if-else, and if-elif-else statements
# Task Number: 3

try:
    temperature
except NameError:
    print("Variable \"temperature\" not defined", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if temperature == 40:
        if re.search("\s*Sunny\s*day\s*", line):
            is_print = True
    elif temperature == 30:
        if re.search("\s*Rainy\s*day\s*", line):
            is_print = True
    else:
        if re.search("\s*Foggy\s*day\s*",line):
            is_print = True

if not is_print:
    print("Please, print weather, that is in task", file=sys.stderr)
    sys.exit(0)

code_string = '\n'.join(user_code_lines)

code_if = False
if re.search('\s*if\s*', code_string):
    code_if = True

code_elif = False
if re.search('\s*elif\s*', code_string):
    code_elif = True

code_else = False
if re.search('\s*else:\s*', code_string):
    code_else = True

if not code_if and not code_elif and not code_else:
    print("Please, use \"if-elif-else\" statements", file=sys.stderr)
    sys.exit(0)


passed_1 = False
passed_2 = False

for line in user_code_lines:
    if re.search("\s*temperature\s*\=\=\s*40\s*", line):
        passed_1 = True
    if re.search("\s*temperature\s*\=\=\s*30\s*", line):
        passed_2 = True



if not (passed_1 and passed_2):
    print("Please, use \"==\", \"if-elif-else\" operators", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))