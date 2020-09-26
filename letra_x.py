import sys
n = int(sys.argv[1])

def letra_x(n):
    if n >=3:
        for i in range(n):
            if i < (n-1)/2:
                print(i*' ' + '*' + (n-2-2*i)*' ' + '*' + i*' ')
            elif i == (n-1)/2:
                print(int((n-1)/2)*' ' + '*' + int((n-1)/2)*' ')
            else:
                print((n-1-i)*' ' + '*' + (n-2-2*(n-1-i))*' '+ '*' + (n-1-i)*' ')
    else:
        print('La letra X se crea sólo con un n > 2')
            
letra_x(n)

