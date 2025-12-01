from abc import ABC, abstractmethod

# -------------------------------
# Interface esperada pelo sistema
# -------------------------------

class PaymentProcessor(ABC):
    """
    Interface formal que define o contrato para qualquer processador de pagamentos.
    A utilização de ABC contribui para a segurança do design e evita implementações incompletas.
    """

    @abstractmethod
    def process_payment(self, amount: float) -> None:
        """
        Processa um pagamento no valor especificado.
        As subclasses devem implementar este método obrigatoriamente.
        """
        pass


# -------------------------------
# Código legado (não pode ser alterado)
# -------------------------------

class LegacyPaymentSystem:
    """
    Classe de um sistema antigo cuja interface é incompatível com a atual.
    O método make_transaction() possui assinatura diferente.
    """

    def make_transaction(self, value: float) -> None:
        print(f"[LEGADO] Pagamento realizado no valor de R$ {value:.2f}")


# -------------------------------
# Adapter
# -------------------------------

class PaymentAdapter(PaymentProcessor):
    """
    Adapter que converte a interface moderna (process_payment)
    para a interface antiga (make_transaction).
    """

    def __init__(self, legacy_system: LegacyPaymentSystem) -> None:
        self._legacy_system = legacy_system

    def process_payment(self, amount: float) -> None:
        """
        Implementação do método da interface moderna.
        Aqui ocorre a chamada adaptada ao sistema legado.
        """
        # Adiciona uma taxa de 1% para o sistema legado
        amount += amount * 0.01
        self._legacy_system.make_transaction(amount)


# -------------------------------
# Uso prático do Adapter
# -------------------------------

legacy = LegacyPaymentSystem()
processor = PaymentAdapter(legacy)

processor.process_payment(150.00)
