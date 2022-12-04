# in your terminal or on the shell in replit.com type in:
# pip install cryptocode
# then you can run this script which contains a hidden flag within it
import cryptocode

a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz{|}()"

#test
cat = input('dog:')
if cat == a[36]+a[51]+a[40]+a[59]:
    j = a[36]+a[51]+a[40]+a[59]
    f = open('flag.txt').read()
    print('the flag is:', cryptocode.decrypt(f,j))