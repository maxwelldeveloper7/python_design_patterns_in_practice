# **Definição do Padrão Factory Method**

O **Factory Method** é um padrão de projeto **criacional** cujo objetivo é **definir uma interface para a criação de objetos**, delegando às subclasses a decisão sobre **qual classe concreta** deve ser instanciada. Ele promove o **desacoplamento** entre o código que solicita um objeto e o código que realmente o cria, permitindo maior flexibilidade, extensibilidade e substituição de implementações sem modificações estruturais no sistema.

---

# **Papéis Fundamentais no Factory Method**

## **1. Criador (Creator)**

É a classe que **declara o Factory Method**, geralmente como um método abstrato ou padrão.
Seu papel é:

* Definir a **interface de criação** de produtos.
* Delegar às subclasses a decisão de qual produto concreto criar.
* Conter operações de alto nível que utilizam o produto retornado pelo Factory Method.

O criador **não sabe** qual classe concreta será instanciada — ele trabalha apenas com a **interface do produto**.

> Em muitos casos, o criador possui um método de lógica geral (ex.: `enviar_notificacao()`) que chama internamente o `factory_method()` para obter o produto correto.

---

## **2. Produto (Product)**

É a **interface ou classe abstrata** que define o comportamento comum de todos os objetos que podem ser criados pelo Factory Method.

Seu papel é:

* Garantir um **contrato comum** entre todas as implementações concretas.
* Permitir que o criador opere sobre tipos genéricos, sem conhecer detalhes de implementação.

As subclasses concretas do produto implementam o comportamento real.

---

## **3. Cliente (Client)**

É o código que **utiliza o criador** para obter produtos.
Seu papel é:

* Solicitar a criação de objetos apenas por meio do **factory method**, sem instanciar classes concretas diretamente.
* Depender exclusivamente das **interfaces** do criador e do produto.

Como consequência, o cliente não precisa conhecer ou alterar código quando novos produtos são adicionados ao sistema.

---

# **Síntese do Funcionamento**

1. O **cliente** chama uma operação no **criador**.
2. O criador invoca o **factory method**.
3. O **factory method**, definido por uma subclasse concreta, instancia o **produto apropriado**.
4. O criador utiliza o produto por meio de sua **interface genérica**.

---

# **Essência Conceitual**

> O Factory Method substitui a criação explícita de objetos (`new`) por uma chamada indireta controlada pelas subclasses, promovendo baixo acoplamento e extensibilidade.

<br><br>

# 📌 **Analogia: A Cozinha de um Restaurante Profissional**

Imagine um restaurante sofisticado que prepara diferentes tipos de pratos conforme a culinária desejada pelo cliente (italiana, japonesa, brasileira, etc.).

## **1. Produto (Product) → O Prato Servido**

O **Produto** representa o **prato final** entregue ao cliente, como:

* Pizza
* Sushi
* Feijoada

Todos são “pratos”, mas cada um tem sua própria implementação.
Assim como no padrão, o *produto* tem uma **interface comum** ("um prato deve poder ser servido"):

> Todos são comidas, todos podem ser servidos, mas cada um é preparado à sua maneira.

---

## **2. Criador (Creator) → A Cozinha**

A **cozinha do restaurante** representa o **Criador**.

* A cozinha tem o *processo padrão* de preparar pedidos.
* Porém, **não define diretamente qual prato será feito**.
* A decisão de *como* preparar depende da **especialidade do chef**.

O **Factory Method** aqui é o equivalente a:

> “Qual é o tipo de prato solicitado? Envie para o chef especializado correspondente.”

A cozinha possui o método **“prepararPrato()”**, mas quem decide qual prato concreto fazer é a **subclasse da cozinha**, ou seja:

* Cozinha Italiana
* Cozinha Japonesa
* Cozinha Brasileira

Cada cozinha especializada implementa o *factory method*:

* A Cozinha Italiana sabe fazer Pizza.
* A Cozinha Japonesa sabe fazer Sushi.
* A Cozinha Brasileira sabe fazer Feijoada.

> A cozinha (Creator) define o processo,
> mas cada cozinha especializada decide *qual prato produzir*.

---

## **3. Cliente (Client) → O Garçom / o App de Pedidos**

O **Cliente** é quem solicita o prato, por exemplo:

* um garçom
* um app de delivery
* um sistema de autoatendimento

O cliente:

* **não precisa saber** quem é o chef
* **não precisa saber** como o prato é feito
* **não conhece a receita**

Ele apenas envia:

> “Preparar prato para mesa X.”

E a **cozinha correta (Creator)** usa o **Factory Method** para determinar *qual tipo de prato concreto* deve ser criado.

---

# 🎯 **Essência da analogia**

* O **Cliente** pede um prato → chama um método de alto nível no Criador.
* O **Criador** segue um fluxo comum de preparo → operação abstrata.
* O **Factory Method** decide qual **Produto** concreto criar → quem implementa isso é a subclasse (cozinha especializada).
* O **Produto** é o prato final entregue.

---

# ✔ **Conexão com o padrão de software**

| Elemento do Padrão   | Elemento da Analogia                     | Função                                                |
| -------------------- | ---------------------------------------- | ----------------------------------------------------- |
| **Creator**          | Cozinha                                  | Define o processo padrão de preparo                   |
| **Factory Method**   | Escolha do chef especializado            | Decide qual prato concreto será produzido             |
| **Concrete Creator** | Cozinha Italiana / Japonesa / Brasileira | Implementa a criação específica                       |
| **Product**          | Prato (Pizza, Sushi, Feijoada)           | Objeto final criado                                   |
| **Client**           | Garçom / App                             | Solicita a criação, mas não sabe como o prato é feito |

---

# ✔ **Frase para memorizar o conceito**

> “No Factory Method, o cliente faz o pedido, o criador administra o processo e a subclasse especializada decide qual produto concreto entregar.”
