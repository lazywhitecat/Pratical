def main():
    sales = float(input('Enter sales:$'))
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print('Bonus is $', bonus, sep='')
    sales = float(input('Enter sales:$'))




#Second question with loop
    while sales >= 0:
        if sales < 1000:
            bonus = sales*0.1
            print(bonus)
            sales = float(input('Enter sales:$'))
        if sales >= 1000:
            bonus = sales*0.15
            print(bonus)
            sales = float(input('Enter sales:$'))
        else:
            break


if __name__ == '__main__':
    main()
