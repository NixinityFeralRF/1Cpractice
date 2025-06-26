print ('Hello GitHub..')

### task 1: RSA
# p, q, e - простые числа

# 1

p = int(input())
q = int(input())

n = p * q
f = (p-1)*(q-1)

e = int(input('простое число, меньше f и простое относительно f: '))

possible_d = []
for d in range(1, 100):
  if (d*e) % f == 1:
    possible_d.append(d)
    
print ('как d можно выбрать одно из этих чисел:', possible_d)

print ('Открытый ключ:', e, n)
print ('Секретный ключ:', d, n)

# 2

encr_mess = (p ** e % n) # это Е

print('Закодированное сообщение, которое можно отправить: ', encr_mess)

# 3

E = encr_mess
decr_mess = E ** d % n
print('Раскодированное полученное сообщение: ', decr_mess)

