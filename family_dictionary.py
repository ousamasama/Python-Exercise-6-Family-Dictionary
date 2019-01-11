# Define a dictionary that contains information about several members of your family. Use the following example as a template.

# my_family = {
#     'sister': {
#         'name': 'Krista',
#         'age': 42
#     },
#     'mother': {
#         'name': 'Cathie',
#         'age': 70
#     }
# }
# Using a dictionary comprehension, produce output that looks like the following example.

# Krista is my sister and is 42 years old
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)

my_family = {
    'brother': {
        'name': 'Mohammed',
        'age': 36
    },
    'nephew': {
        'name': 'Malik',
        'age': 1.8
    },
    'dad': {
        'name': 'Mustafa',
        'age': 84
    }
}

dictionary_comprehension = {f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old' for (family_member, member_values) in my_family.items()}
print(dictionary_comprehension)