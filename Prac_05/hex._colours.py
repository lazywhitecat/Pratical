colour_dict = {'AliceBlue': '#f0f8ff', 'AntiqueWhite': '#faebd7', 'AntiqueWhite1': '#ffefdb',
               'AntiqueWhite2': '#eedfcc', 'AntiqueWhite3': '#cdc0b0', 'AntiqueWhite4': '#8b8378',
               'aquamarine1': '#7fffd4', 'aquamarine2': '#76eec6', 'aquamarine4': '#458b74', 'azure1': '#f0ffff'}
choose_colour = input('Enter your color name:')
while choose_colour != '':
    if choose_colour in colour_dict:
        print(choose_colour, 'is', colour_dict[choose_colour])
    else:
        print('Invalid colour name.')
    choose_colour = input('Enter your color name:')
