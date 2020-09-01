from Prac_06.guitar import Guitar
def main():
    guitars = []
    name = input('Name:')
    while name != '':
        year = int(input('Year:'))
        cost = int(input('Cost: $'))
        add_to_guitars = Guitar(name,year,cost)
        guitars.append(add_to_guitars)
        print('{} ({}) :{} added'.format(name,year,cost))
        name = input('Name:')
    if guitars != '':
        print('There are my guitars:')
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage(guitar.get_age()):
                vintage_string = "(vintage)"
            print("Guitar {}: {:>5} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
    else:
        print('No guitars are showed.')
main()