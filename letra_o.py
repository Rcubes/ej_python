import sys
n = int(sys.argv[1])


def letra_o(n):
    if n >= 3:
        top_bot = n *'*' 
        lat = '*'+ ' '*(n-2) + '*'

        print(top_bot)
        for i in range(n-2):
            print(lat)
        print(top_bot)
    else:
        print('La letra O se crea sólo con un n > 2')

letra_o(n)