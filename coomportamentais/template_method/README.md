# Template Method - Gerador de Relatórios

## O que é o Template Method?

O Template Method define o esqueleto de um algoritmo em uma classe base, permitindo que subclasses implementem etapas específicas sem alterar a estrutura geral.

## Implementação
![](../../assets/img/template_method.png)
### Classe Base Abstrata
```python
class ReportGenerator(ABC):
    def generate(self):  # Template Method
        data = self.load_data()
        processed = self.process_data(data)
        self.export(processed)
```

### Classes Concretas
- **SalesReport**: Relatório de vendas com soma total
- **InventoryReport**: Relatório de estoque com desconto de itens reservados

## Código
```python
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

```

## Como Executar

```python
python exemplo_template_method.py
```

## Saída
```
=== Relatório de Vendas ===
Carregando dados de vendas...
Processando dados de vendas...
Exportando relatório de vendas: total = R$ 450

=== Relatório de Estoque ===
Carregando dados de estoque...
Processando dados de estoque...
Exportando relatório de estoque:
 - camisetas: 110 itens disponíveis
 - calças: 70 itens disponíveis
 - sapatos: 40 itens disponíveis
```

## Vantagens
- Reutiliza o algoritmo principal
- Permite variações específicas
- Facilita manutenção e extensão