# try and except

try:
    f = open('a.txt', 'r')
    f.close()
    #f.read()
    a = 1
    len(a)
except FileNotFoundError:
    print('ok')

except ValueError as e:
    print(e)
