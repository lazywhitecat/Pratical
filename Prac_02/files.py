user_name = str(input('Enter your name:'))
name_file = 'name.txt'
name_files = open(name_file,'w')
print('Your name is {}'.format(user_name),file = name_files)
name_files.close()


number_file = 'numbers.txt'
number_files = open(number_file,'r')
line_one = number_files.readline()
line_two = number_files.readline()
first_line = int(line_one)
second_line = int(line_two)
print(first_line+second_line)

all_lines = number_files.readline()
print(all_lines)