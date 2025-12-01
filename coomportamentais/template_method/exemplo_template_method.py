from abc import ABC, abstractmethod


# =============================================================
# TEMPLATE METHOD — Classe base com algoritmo estruturado
# =============================================================
class ReportGenerator(ABC):
    """
    Classe abstrata que define o fluxo geral para geração de relatórios.
    O método template 'generate()' é fixo e não deve ser sobrescrito.
    As subclasses definem apenas a lógica específica de cada etapa.
    """

    def generate(self) -> None:
        """
        Template Method.
        Define o fluxo de geração de um relatório, chamando etapas
        que podem ser personalizadas pelas subclasses.
        """
        data = self.load_data()
        processed = self.process_data(data)
        self.export(processed)

    @abstractmethod
    def load_data(self):
        """Carrega os dados necessários para o relatório."""
        pass

    @abstractmethod
    def process_data(self, data):
        """Realiza o processamento específico dos dados."""
        pass

    @abstractmethod
    def export(self, processed):
        """Gera a saída final do relatório."""
        pass


# =============================================================
# CONCRETE CLASSES — Implementam variações do algoritmo
# =============================================================
class SalesReport(ReportGenerator):
    """Relatório de vendas."""

    def load_data(self):
        print("Carregando dados de vendas...")
        return [100, 200, 150]

    def process_data(self, data):
        print("Processando dados de vendas...")
        return sum(data)

    def export(self, processed):
        print(f"Exportando relatório de vendas: total = R$ {processed}")


class InventoryReport(ReportGenerator):
    """Relatório de estoque."""

    def load_data(self):
        print("Carregando dados de estoque...")
        return {"camisetas": 120, "calças": 80, "sapatos": 50}

    def process_data(self, data):
        print("Processando dados de estoque...")
        return {k: v - 10 for k, v in data.items()}  # Desconta itens reservados

    def export(self, processed):
        print("Exportando relatório de estoque:")
        for item, qtd in processed.items():
            print(f" - {item}: {qtd} itens disponíveis")


# =============================================================
# Exemplo de uso
# =============================================================
if __name__ == "__main__":
    print("=== Relatório de Vendas ===")
    SalesReport().generate()

    print("\n=== Relatório de Estoque ===")
    InventoryReport().generate()
