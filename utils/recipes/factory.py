"""Module that create faker data for testing the aplication."""
from random import randint

from faker import Faker

fake = Faker()


def rand_ratio():
    """Function that radomly chooses the size of the image cover in the
    function make_recipe.
    Return tuple
    """
    return randint(840, 900), randint(473, 573)


def make_recipe():
    """Function that create recipe.
    Return dict
    """
    return {
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': f'https://loremflickr.com/{rand_ratio()[0]}/'
                   f'{rand_ratio()[1]}/food,cook',
        }
    }


def make_person():
    """Function that create name, address and a description for a person."""
    return {
        'name': fake.name(),
        'address': fake.address(),
        'description': fake.text()
    }


if __name__ == '__main__':
    persons = make_person()
    for key, value in persons.items():
        print(f'{key}: {value}')
    print()
    recipe = make_recipe()
    for key, value in recipe.items():
        print(f'{key}: {value}')
