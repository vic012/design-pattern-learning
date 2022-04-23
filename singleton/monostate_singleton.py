#A monostate happens when you have different instances of a class that share the same state.


class Monostate:
	#I'm declaring a state of the type dict for this class
	#Soon all object instantiated will have the same state

	#State can also be understood how "Class Attributes"

	__state = {} #This is an what will it be shared class attribute with all instances

	def __new__(cls, *args, **kwargs):
		obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
		obj.__dict__ = cls.__state
		return obj

instance1 = Monostate() #1ª instance
print(f'Id: {id(instance1)}')
print(instance1.__dict__) #Will return one {} (Empty)

instance2 = Monostate() #2ª instância
print(f'Id: {id(instance2.__dict__)}')
print(instance2.__dict__) #Will return one {} (Empty)

#Creating a new attribute through instance1
instance1.nome = "Monostate Singleton"

print(f'1ª Instance: {instance1.__dict__}')
print(f'2ª Instance: {instance2.__dict__}')
