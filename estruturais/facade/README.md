# Sistema de Pedidos - Padrão Facade

## Cenário:
Imagine que um módulo de processamento de pedidos envolve diversas etapas internas:
- Verificar estoque
- Processar pagamento
- Emitir nota
- Organizar entrega

O cliente não deve lidar com a complexidade do subsistema.
Assim, criamos uma **fachada** (***OrderFacade***) que expõe um método simples: ***place_order()***.

## Sobre o Padrão Facade

O padrão Facade fornece uma interface unificada e simplificada para um conjunto de interfaces mais complexas em um subsistema. Ele define uma interface de nível mais alto que torna o subsistema mais fácil de usar.

## Estrutura do Sistema
![](../../assets/img/facade.png)
### Subsistemas Complexos

#### `InventorySystem` (Sistema de Estoque)
- `check_stock(product_id)`: Verifica disponibilidade do produto

#### `PaymentSystem` (Sistema de Pagamento)
- `process_payment(value)`: Processa o pagamento do pedido

#### `InvoiceSystem` (Sistema de Nota Fiscal)
- `generate_invoice(product_id, value)`: Emite nota fiscal

#### `ShippingSystem` (Sistema de Entrega)
- `arrange_delivery(product_id)`: Organiza a entrega do produto

### `OrderFacade` (Fachada)
Interface simplificada que coordena todos os subsistemas:
- `place_order(product_id, value)`: Executa todo o fluxo de pedido

## Fluxo do Pedido

1. **Verificação de estoque** - Confirma disponibilidade
2. **Processamento de pagamento** - Valida e processa pagamento
3. **Emissão de nota fiscal** - Gera documentação fiscal
4. **Organização da entrega** - Prepara envio do produto

## Código

```python
# ---------------------------------------------------------
# Subsistemas (complexos, mas independentes entre si)
# ---------------------------------------------------------

class InventorySystem:
    """Responsável pelo estoque."""

    def check_stock(self, product_id: int) -> bool:
        """Simula uma verificação de estoque."""
        print(f"[Estoque] Verificando disponibilidade do produto {product_id}...")
        return True


class PaymentSystem:
    """Responsável pelo pagamento."""

    def process_payment(self, value: float) -> bool:
        """Simula o processamento de pagamento."""
        print(f"[Pagamento] Processando pagamento de R$ {value:.2f}...")
        return True


class InvoiceSystem:
    """Responsável pela emissão de nota fiscal."""

    def generate_invoice(self, product_id: int, value: float) -> None:
        """Simula a geração de nota."""
        print(f"[Nota Fiscal] Emitindo NF para produto {product_id} no valor de R${value:.2f}.")


class ShippingSystem:
    """Responsável pelo envio do produto."""

    def arrange_delivery(self, product_id: int) -> None:
        """Simula organização da entrega."""
        print(f"[Entrega] Organizando envio do produto {product_id} para o cliente.")


# ---------------------------------------------------------
# Facade (interface simples para o subsistema)
# ---------------------------------------------------------

class OrderFacade:
    """
    Fornece uma interface simplificada para criar um pedido.
    Encapsula a complexidade dos sistemas internos.
    """

    def __init__(
        self,
        inventory: InventorySystem,
        payment: PaymentSystem,
        invoice: InvoiceSystem,
        shipping: ShippingSystem
    ) -> None:

        self._inventory = inventory
        self._payment = payment
        self._invoice = invoice
        self._shipping = shipping

    def place_order(self, product_id: int, value: float) -> None:
        """
        Realiza todas as etapas internas de um pedido.
        O cliente precisa apenas chamar este método.
        """

        if not self._inventory.check_stock(product_id):
            print("Pedido não realizado: produto sem estoque.")
            return

        if not self._payment.process_payment(value):
            print("Pedido não realizado: pagamento recusado.")
            return

        self._invoice.generate_invoice(product_id, value)
        self._shipping.arrange_delivery(product_id)

        print("\n[Pedido] Pedido concluído com sucesso!")


# ---------------------------------------------------------
# Uso prático do Facade
# ---------------------------------------------------------

# Instanciando subsistemas
inventory = InventorySystem()
payment = PaymentSystem()
invoice = InvoiceSystem()
shipping = ShippingSystem()

# Criando a fachada
order_service = OrderFacade(inventory, payment, invoice, shipping)

# Cliente utiliza apenas a fachada
order_service.place_order(product_id=123, value=299.90)

```

## Execução

```bash
python exemplo_facade.py
```

**Saída esperada:**
```
[Estoque] Verificando disponibilidade do produto 123...
[Pagamento] Processando pagamento de R$ 299.90...
[Nota Fiscal] Emitindo NF para produto 123 no valor de R$299.90.
[Entrega] Organizando envio do produto 123 para o cliente.

[Pedido] Pedido concluído com sucesso!
```

## Vantagens do Facade

- **Simplicidade**: Interface única para operações complexas
- **Desacoplamento**: Cliente não precisa conhecer subsistemas internos
- **Manutenibilidade**: Mudanças internas não afetam o cliente
- **Reutilização**: Fachada pode ser usada por diferentes clientes

## Casos de Uso Práticos

- APIs que agregam múltiplos serviços
- Sistemas de e-commerce com múltiplas etapas
- Bibliotecas que simplificam frameworks complexos
- Interfaces para sistemas legados com múltiplos componentes

## Diferença Sem o Facade

Sem o padrão, o cliente precisaria:
```python
# Cliente gerenciando toda a complexidade
if inventory.check_stock(123):
    if payment.process_payment(299.90):
        invoice.generate_invoice(123, 299.90)
        shipping.arrange_delivery(123)
```

Com o Facade, apenas:
```python
# Cliente usa interface simples
order_service.place_order(123, 299.90)
```