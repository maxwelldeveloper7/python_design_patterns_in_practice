import copy

class Prototype:
    """
    Interface base com o método de clonagem.
    Garante que todas as classes concretas implementem clone().
    """
    def clone(self):
        raise NotImplementedError("A subclasse deve implementar clone().")


class Document(Prototype):
    """
    Classe concreta que possui atributos que podem ser clonados.
    Representa um documento personalizável.
    """

    def __init__(self, title, content, metadata):
        # Atributos principais do documento.
        self.title = title
        self.content = content
        
        # Metadados: dicionário com informações adicionais.
        # Deve ser clonado profundamente.
        self.metadata = metadata  

    def clone(self):
        """
        Cria uma cópia profunda do objeto.
        Deep copy é essencial quando há estruturas mutáveis (listas, dicts etc.).
        """
        return copy.deepcopy(self)

    def __str__(self):
        """Retorna uma representação amigável para inspeção."""
        return f"Document(title={self.title}, content={self.content}, metadata={self.metadata})"


# ------------ USO PRÁTICO ------------ #

# Documento base que servirá como protótipo.
prototype_doc = Document(
    title="Template Básico",
    content="Conteúdo padrão do documento.",
    metadata={"author": "Sistema", "version": 1}
)

# Produzindo novos documentos por clonagem.
invoice = prototype_doc.clone()
invoice.title = "Nota Fiscal"
invoice.metadata["document_type"] = "NFe"

report = prototype_doc.clone()
report.title = "Relatório Financeiro"
report.metadata["document_type"] = "Report"

# Visualização
print(invoice)
print(report)
