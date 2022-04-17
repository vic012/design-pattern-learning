The singleton pattern is used to get an instance of an object, a type, a global hotspot.

quote from refactor: "https://refactoring.guru/pt-br/design-patterns/singleton"

"Todas as implementações do Singleton tem esses dois passos em comum:

1 - Fazer o construtor padrão privado, para prevenir que outros objetos usem o operador new com a classe singleton.

2 - Criar um método estático de criação que age como um construtor. Esse método chama o construtor privado por debaixo dos panos para criar um objeto e o salva em um campo estático. Todas as chamadas seguintes para esse método retornam o objeto em cache.
Se o seu código tem acesso à classe singleton, então ele será capaz de chamar o método estático da singleton. Então sempre que aquele método é chamado, o mesmo objeto é retornado."