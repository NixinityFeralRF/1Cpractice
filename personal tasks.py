### task 1: RSA

# мой вариант 7-й, и числа мне достались p = 11 и q = 11
# повезло как обычно, такие разные <3

# 1

p = 7     # с такими значениями
q = 17    # все работает как надо

n = p * q             #121, если p = 11 и q = 11
f = (p-1)*(q-1)       #100, если p = 11 и q = 11

print('n и f:', n, f)

possible_e1 = [2,]
possible_e2 = []

for E in range(3, f):
  pr = 1
  for num in possible_e1:
    if E % num == 0:
      pr = 0
  if pr == 1 and f > E:
    possible_e1.append(E)

for E2 in possible_e1:
  if f % E2 != 0:
    possible_e2. append(E2)

print('Просто простые числа меньше f:        ', possible_e1)
print('Число e может быть один из этих чисел:', possible_e2)

e = 13     #решил такое число взять, стандарту соответствует

possible_d = [0,]
for D in range(1, n):
  if (D*e) % f == 1:
    possible_d.append(D)
    
print ('как d можно выбрать одно из этих чисел:', possible_d)
d = possible_d[-1]

print ('Открытый ключ (e,n): ', e, n)
print ('Секретный ключ (d,n): ', d, n)

# 2

M = int(input('Введите число, которое нужно передать: '))
encr_mess = ((M ** e) % n) # это Е

print('Закодированное сообщение, которое можно отправить:', encr_mess)

# 3

E = encr_mess
decr_mess = ((E ** d) % n)
print('Раскодированное полученное сообщение:', decr_mess)




  
### task 2: Diffie-Hellman

def DF(g, p, a, b):
  print(f'Числа: g = {g}, p = {p}, a = {a}, b = {b}')
  A = ((g**a) % p)
  B = ((g**b) % p)
  print('Числа которые они передают друг другу:', A, B)

  FcodeA = ((B**a) % p)
  FcodeB = ((A**b) % p)
  print('Секретный ключ равный у обоих:', FcodeA, FcodeB)

DF(43, 3,  1, 1)
DF(29, 9,  3, 4)
DF(27, 24, 2, 3)
DF(81, 14, 5, 2)
DF(17, 9,  1, 4)

