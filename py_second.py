

##n = int(input('> '))
##
##print(n + n % 10)

##x = 10
##y = 10
##
##if  x < y:
##    print('X < Y')
##elif x > y:
##    print('X > Y')
##else:
##    print('X = Y')


##h = input('введите время суток: ')
##if not h.isdigit():
##    exit(0)
##h = int(h)    
##if h >= 4 and h < 12:
##    print('Morning')
##elif 12 <= h < 17:
##    print('Day')
##elif h >= 17 and h < 24:
##    print('Evening')
##elif h >= 0 and h < 4 or h ==24:
##    print('Night')
##else:
##    Print('Время суток не соответствует.')


##    
##color = input('введите цвет светофора: ')
##
##match color:
##    case 'red'| 'no': print('STOP')
##    case 'green': print('GO')
##    case 'yellow': print('READY')
##    case _:print('цвет -', color)

"""
  00   0
  01   1
  10   2
  11   3
 100   4
 101   5
 110   6
 111   7
1000   8
1001   9
1010  10


"""
num = input('Число в двоичной системе > ')
print('Число в десятичной системе >' , end=' ')
match num:
    case '0': print(0)
    case '1': print(1)
    case '10': print(2)
    case '11': print(3)
 
    
    
