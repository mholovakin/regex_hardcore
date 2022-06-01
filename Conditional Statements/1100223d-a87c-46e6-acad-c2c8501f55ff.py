# Course: Python Course
# Section: Conditional Statements
# Chapter: What are the conditional statements?
# Task Number: 1

try:
    number
except NameError:
    print("Variable \"number\" not defined", file=sys.stderr)
    sys.exit(0)


is_print = False
for line in user_print_lines:
    if number >= 1:
        if line == 'Positive':
            is_print = True
    elif number <= -1:
        if line == 'Negative':
            is_print = True
    else:
        if line == "Zero":
            is_print = True

if not is_print:
    print("Please, print condition of variable, using \"if-elif-else\" statements", file=sys.stderr)
    sys.exit(0)

code_string = '\n'.join(user_code_lines)
num_more = False
if re.search('\s*number\s*>=\s*1\s*', code_string):
    num_more = True

num_less = False
if re.search('\s*number\s*<=\s*-1\s*', code_string):
    num_less = True

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

if not (num_more and num_less):
    print("Please, use \"if-elif-else\" statements with greater than or equal and less than or equal operators", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))