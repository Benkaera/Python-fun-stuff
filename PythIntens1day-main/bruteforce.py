import requests
#alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
#0 0
#10 A
#16 10
#20 14

# alphabet = '0123456789ABCDEF'
#i = 1000
#result = ''
#while i>0:
#    n = i // 16
#    rest = i % 16
#    result = alphabet[rest] + '|' + result
#    i = n








alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)

i = 0
length = 0

while True:

    result = ''
    temp = i
    while temp > 0:
        rest = temp % base         # остаток от дел
        result = alphabet[rest] + result
        temp = temp // base           #целочисл делен



    while len(result) < length:
        result = '0' + result

    #print(result)
    data = {'login': 'admin', 'password': result}
    response = requests.post('http://127.0.0.1:5000/auth', json=data)
    if response.status_code == 200:
        print('SUCCES!', result)
        break

    if result == 'z' * length:
        length += 1
        i = 0
    else:
        i += 1

    i += 1