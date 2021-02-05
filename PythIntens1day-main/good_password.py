import random

def generate_good_pass(length):

  # 1) задать алфавит 'abc'.upper
  # random.choice('abc')
  alphabet = 'abcdefghijklmnopqrstuvwxyz'\
              'ABCDEFGHIJKLMNOPQRSTUVWXYZ'\
              '0123456789!@#$%^&*()_+=-,.?'

  # return ''.join(random.choices(alphabet, k=length))

  # 2) выбрать случайный символ из алфавита
  # 3) повторить  2 length раз
  # 4) склеить символы в строку
  password = ''
  for i in range(length):
    symbol = random.choice(alphabet)
    password += symbol

  return password


#print(generate_good_pass(1))
#print(generate_good_pass(10))
#print(generate_good_pass(30))


popular_passes = [
  '1234',
  'admin',
  'qwerty',
  '234242'
]


print('-------')



popular_pas_data = '''password

'''

popular_passes = popular_pas_data.split('\n')
print(popular_passes[:10])
print(len(popular_passes))

i = 0

def generate_bad_password():
  global i

  if i >= len(popular_passes):
    return

  #use popular passes
  password = popular_passes[i]
  i += 1
  return password



for i in range(100):
  print(generate_bad_password())




###print(generate_bad_password())
#print(generate_bad_password())
#print(generate_bad_password())
#print(generate_bad_password())
#print(generate_bad_password())
#print(generate_bad_password())
