def fizzbuzz(num):
  for n in range(1,num):
    if n % 3 == 0 and n % 5 == 0:
        print 'FizzBuzz'
    elif n % 3 == 0:
        print 'Fizz'
    elif n % 5 == 0:
        print 'Buzz'
    else:
        print n

fizzbuzz(20)
