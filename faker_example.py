from faker import Faker

faker = Faker()

user_data = {"name": faker.name(), "email": faker.email(), "address": faker.address()}

print(faker.name())
print(faker.address())
print(faker.email(domain="mail.ru"))
