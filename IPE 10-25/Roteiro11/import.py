from faker import Faker
from random import randint

fake = Faker('pt_BR')

print("Nome:", fake.name())
print("Endereço:", fake.address())
print("Email:", fake.email())

nota01 = randint(1, 10)
nota02 = randint(1, 10)

print(f"Primeira nota: {nota01:.2f}")
print(f"Segunda nota: {nota02:.2f}")