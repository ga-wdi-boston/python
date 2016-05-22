def fizzbuzz(max_num):
    """Loops through 1-max_num and prints message depending on evaluation of integer."""
    for num in range(1, max_num):
        if num % 3 == 0 and num % 5 == 0:
            print 'FizzBuzz'
        elif num % 3 == 0:
            print 'Fizz'
        elif num % 5 == 0:
            print 'Buzz'
        else:
            print num

fizzbuzz(20)
