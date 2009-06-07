''' Load and store configuration.

    config is a dictionary storing key:value pairs of absolutely anything,
including additional dictionaries.
'''

global config

def load():
    config = {
        'username':'zeiris',
        'password':'secret',
        'mingamelength':3   # seconds
        }

