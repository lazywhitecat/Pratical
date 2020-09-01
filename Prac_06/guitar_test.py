from Prac_06.guitar import Guitar
def main():
    guitar = Guitar("Gibson L-5 CES",year = 1922,cost = 16035.40)
    print('{}'.format(guitar.get_age()))
    print('{}'.format(guitar.is_vintage(guitar.get_age())))
main()