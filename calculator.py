def display_menu():
    print('Welcome to Shra\'s Calculator\n'
          '1.Addition\n'
          '2.Subtraction\n'
          '3.Multiplication\n'
          '4.Division\n'
          '5.Square\n'
          '6.Mods\n')

def perform_operation(operation):
    number = int(input('please enter number 1'))
    if operation == 1:
        number_2 = int(input('please enter number 2'))
        print('addition of %d and %d is %d'% (number,number_2,number + number_2))
    elif operation == 2:
        number_2 = int(input('please enter number 2'))
        print('subtraction of %d and %d is %d' % (number, number_2, number - number_2))
    elif operation == 3:
        number_2 = int(input('please enter number 2'))
        print('multiplication of %d and %d is %d' % (number, number_2, number * number_2))
    elif operation == 4:
        number_2 = int(input('please enter number 2'))
        print('division of %d and %d is %d' % (number, number_2, number / number_2))
    elif operation == 5:
        number = int(input('please enter a number '))
        print('square of %d is %d' % (number, number * number))
    else:
        number_2 = int(input('please enter number 2'))
        print('remainder of %d and %d is %d' % (number, number_2, number % number_2))

if __name__ == '__main__':
    display_menu()
    operation = int(input('which operation do you want to perform'))
    if(operation < 1 or operation > 6):
        print('Please select valid operation')
    else:
        perform_operation(operation)