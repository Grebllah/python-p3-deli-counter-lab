def line(line):
    print_output = []
    index = 0
    while index < len(line):
        print_output.append(f" {index + 1}. {line[index]}")
        index += 1
    printout = ''.join(print_output)  
    if len(line) == 0:
        print('The line is currently empty.')
    else:
        print(f"The line is currently:{printout}")

def take_a_number(line, new_cust):
    line.append(new_cust)
    new_number = len(line)
    print(f"Welcome, {new_cust}. You are number {new_number} in line.")

def now_serving(line):
# Build the `now_serving()` function which should call out (`print`) the next
# person in line and then remove them from the front. If there is nobody in line,
# it should call out (`print`) that `"There is nobody waiting to be served!"`.
    if len(line) == 0:
        print("There is nobody waiting to be served!")
    else:
        current_cust = line.pop(0)
        print(f"Currently serving {current_cust}.")
    pass

