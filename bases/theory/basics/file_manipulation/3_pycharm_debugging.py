if __name__ == '__main__':

    # slicing
    print(' === slicing === ')
    my_str = 'abcdefghax'
    print(my_str[0])
    print(my_str[-1])

    print(my_str[0:3])
    print(my_str[::2])
    print(my_str[::-1])

    # String methods
    print(my_str.replace('a', 'z'))
    print(my_str.index('fgh'))
    print('bcdf' in my_str)

    my_str = 'Hello python world!'
    print(my_str.split())

    # formatting
    print(' === formatting === ')
    age = 26
    firstname = 'Luc'

    print(f'My name is {firstname} and I\'m {age}')
    print('My name is %s and I\'m %s' % (firstname, age))

    data_dict = {'firstname': firstname, 'age': age, 'nationality': 'CH'}
    print("My name is %(firstname)s and I'm %(age)s" % data_dict)

    # Don't do it at home!
    print('My name is ' + firstname + ' and I\'m ' + str(age))

    # Print multiple variables at once
    print('My name is', firstname, 'and I\'m', age)
    
