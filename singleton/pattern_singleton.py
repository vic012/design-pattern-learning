

class Singleton:

    #__new__ is a class method that will create the object
    def __new__(cls):
        # hasattr checks if the instance is an attribute of the Singleton class, if there is not create an new instance
        if not hasattr (cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print('Created an new instance')
            return cls.instance
        # else return the existing instance
        print('Return an instance existing')
        return cls.instance

singleton_init = Singleton() # create an new instance
print(f'Instance 1: {id(singleton_init)}')
singleton_repeat = Singleton() # return the existing instance
print(f'Instance 2: {id(singleton_repeat)}')