#day 2: 30 Days of Python programming
first_name, last_name, country, city, age, is_married = input("what is your first name? "), 'Doe', 'USA', 'New York', input("what is your age? "), False
skills = ['Python', 'JavaScript', 'SQL']

person_info = {
    'first_name': first_name,
    'last_name': last_name,
    'country': country,
    'city': city,
    'age': age,
    'is_married': is_married,
    'skills': skills
}


# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

