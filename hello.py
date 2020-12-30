print('hello world!')

import factory

from faker import Factory

faker = Factory.create()

print(faker.uuid4())


profile1 = faker.simple_profile()
print(profile1)
sex = profile1['sex']
print(f' gender code: {sex}')

print(f'Boolean: {faker.pybool()}')

print(f'Date: {faker.date()}')

print(f'Claim Number (any number as string): {str(faker.pyint())}')

print(f'first_name: {faker.first_name()}')
print(f'last_name: {faker.last_name()}')

print(f'street_address: {faker.street_address()}')
print(f'address:: {faker.address()}')
print(f'zipcode: {faker.state_abbr()}')
print(f'country_code: {faker.country_code()}')
print(f'zipcode: {faker.postcode()}')
print(f'Decimal Field: {faker.pydecimal(left_digits=3, right_digits=2, positive=True, min_value=None, max_value=None)}')



if __name__ == '__main__':
    pass




