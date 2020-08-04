def main():
    #temperature conversion system
    determine_temperature_type = input('Enter your temperature type in celsius(c) or fahrenheit(f):')
    while True:
        if determine_temperature_type == 'c':
            celsius_value = float(input('Enter your celsius number:'))
            fahrenheit = convert_celsius_to_fahrenheit(celsius_value)
            print('The fahrenheit value is {:.2f}'.format(fahrenheit))
            break
        elif determine_temperature_type == 'f':
            celsuis_value = float(input('Enter your fahrenheit number:'))
            celsius = convert_fahrenheit_to_celsius(celsuis_value)
            print('The celsius value is {:.2f}'.format(celsius))
            break
        else:
            print('Invalid temperature type')
            determine_temperature_type = input('Enter your temperature type in celsius(c) or fahrenheit(f):')
def convert_celsius_to_fahrenheit(temperature):
    #convert celsius to fahrenheit
    return 9 / 5 * temperature + 32

def convert_fahrenheit_to_celsius(temperature):
    #convert fahrenheit to celsius
    return 5 / 9 * (temperature-32)


main()