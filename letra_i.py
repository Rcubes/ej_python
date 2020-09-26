import sys
n = int(sys.argv[1])


def letra_i(n):
    
    if n >= 3:
        top_bot = n*'*'
        if n % 2 == 0:
            middle = int(n/2 -1)*' ' + '**' +  int(n/2 -1)*' '
        else:
            middle = int((n-1)/2)*' ' + '*' +  int((n-1)/2)*' '
    
        print(top_bot)
        for i in range(n-2):
            print(middle)
        print(top_bot)
    else: 
        print('La letra I se crea sólo con un n > 2')

letra_i(n)