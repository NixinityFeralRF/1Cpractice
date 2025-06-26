print ('Hello GitHub..')

### task 1: RSA
# p, q, e - простые числа

# 1

p = int(input())
q = int(input())

n = p * q
f = (p-1)*(q-1)

e = int(input(f'Введите простое число, меньше {f} и простое относительно {f}: '))

possible_d = [0,]
for D in range(1, n):
  if (D*e) % f == 1:
    possible_d.append(D)
    
print ('как d можно выбрать одно из этих чисел:', possible_d)
d = possible_d[-1]

print ('Открытый ключ (e,n): ', e, n)
print ('Секретный ключ (d,n): ', d, n)

# 2

M = int(input('Введите сообщение для кодировки: '))
encr_mess = ((M ** e) % n) # это Е

print('Закодированное сообщение, которое можно отправить: ', encr_mess)

# 3

E = encr_mess
decr_mess = ((E ** d) % n)
print('Раскодированное полученное сообщение: ', decr_mess)

# извиняюсь если мой код непонятный
