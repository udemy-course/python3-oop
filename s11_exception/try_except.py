

try:
    f = open('a.txt', 'r')
    f.close()
except FileNotFoundError:
    print('ok')



print('finished')
