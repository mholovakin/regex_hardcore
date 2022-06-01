# Course: Python Course
# Section: Types and Variables
# Chapter: String Special Operations
# Task Number: 3

try:
    sentence
except NameError:
    print("Variable \"sentence\" not defined", file=sys.stderr)
    sys.exit(0)

if sentence != 'I was leaving for the airport from the hotel.':
    print("Please, use variable initial value", file=sys.stderr)
    sys.exit(0)

string = ""
for line in user_code_lines:
    if re.search('print', line):
        string = line

if string == "":
    print("Please, print the result of sentence check", file=sys.stderr)
    sys.exit(0)

is_for_while = False
if re.search('(for.*while)|(while.*for)', string):
    is_for_while = True

is_in_sentence = False
if re.search('\s*in\s*.*sentence\s*', string):
    is_in_sentence = True

if not (is_for_while and is_in_sentence):
    print("Pleae, use \"in\" operator and check \"sentence\" variable", file=sys.stderr)
    sys.exit(0)

print(json.dumps({'token': '{{token}}', 'passed': True}))