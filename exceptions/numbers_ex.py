while True:

    print('Give me two numbers')
    try:
        first_numbers = input('Give me a first numbers ! \n')
        first_numbers = int(first_numbers)
        second_number = input('Give me a second number\n')
        second_number = int(second_number)

        summary = first_numbers + second_number
        print(f'The summary of tow numbers is {summary}')
        break

    except ValueError:
        print('Sorry i really need a number!!!!!')

