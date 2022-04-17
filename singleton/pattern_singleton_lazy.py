# The lazy module allows instantiating an object even if it is not used at the same time,
# in this way the object will only be created when it is used


class Singleton:


    # Attr private
    _instance = None

    def __init__(self):
        if not Singleton._instance:
            print('O método __init__ foi chamado...')
        else:
            print(f'A instância já foi criada: {self.get_instance()}')

    # Only here the object is created when this method is called
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = Singleton()
        return cls._instance


singleton_init = Singleton() # class initialized, but the object was not created
print(f'Create object: {singleton_init.get_instance()}') #Instance created
singleton_repeat = Singleton() # return the existing instance