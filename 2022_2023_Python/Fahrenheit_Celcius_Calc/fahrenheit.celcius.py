print("Greetings! This is a measurement conversion program")


program_running = False

fahrenheit = 0
celcius = 0

while program_running is False:
    switch = input('If you would like to quit type in: \"end\"\n\nWhich measurement would you like to convert?\nPlease write \"Fahrenheit\" or \"Celcius\". ').lower()
    
    if switch == "celcius":
        convert_celcius = int(input("Please type in the Celcius temperature you would like to convert: "))
        for degree in range(convert_celcius):
            fahrenheit = int((convert_celcius * 9 / 5) + 32)
        print(f'-------------\n{convert_celcius}°C is {fahrenheit}°F.\n-------------')

    elif switch == "fahrenheit":
        convert_fahrenheit = int(input("Please type in the Fahrenheit temperature you would like to convert: "))
        for degree2 in range(convert_fahrenheit):
            celcius = int((convert_fahrenheit - 32) * 5 / 9)
        print(f'-------------\n{convert_fahrenheit}°F is {celcius}°C\n-------------')
        
    elif switch == "end":
        program_running = True 
    else:
        print("----------------------\nYour input is invalid. \n----------------------")
    pass
