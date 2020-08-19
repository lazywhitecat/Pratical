my_dict = {}
input_email = input('Enter your email:')
while input_email != ' ':
    email_name = input_email.split('@')
    full_name = email_name[0].split('.')
    full_name =' '.join(full_name).title()
    print(full_name)
    my_dict[full_name] = input_email
    input_email = input('Enter your email:')
