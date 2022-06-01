# Course: Python Course
# Section: Conditional Statements
# Chapter: Nested if Conditions
# Task Number: 1

try:
    variable_a
except NameError:
    print("Variable \"variable_a\" not defined", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if variable_a > 25:
        if variable_a < 30:
            if line == "The number is greater than 25 but less than 30":
                is_print = True
        else:
            if line == "The number is greater than 30":
                is_print = True
    else:
        if line == "The number is less than 25":
            is_print = True


if not is_print:
    print("Please, print lines which are indicated in the task, using \"if-else\" statements", file=sys.stderr)
    sys.exit(0)

counter_if = 0
counter_else = 0

for line in user_code_lines:
    if re.search('\s*if\s*', line):
        counter_if = counter_if + 1
    if re.search('\s*else:\s*', line):
        counter_else = counter_else + 1

if counter_if != 2:
    print("Please, use \"if\" statement twice", file=sys.stderr)
    sys.exit(0)

if counter_else != 2:
    print("Please, use \"else\" statement twice", file=sys.stderr)
    sys.exit(0)

code_string = '\n'.join(user_code_lines)
greater_25 = False
if re.search('\s*variable_a\s*>\s*25\s*', code_string):
    greater_25 = True

less_30 = False
if re.search('\s*variable_a\s*<\s*30\s*', code_string):
    less_30 = True

if not (greater_25 and less_30):
    print("Please, code comparison between variable_a and 25 and comparison between variable_a and 30", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))