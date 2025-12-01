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
