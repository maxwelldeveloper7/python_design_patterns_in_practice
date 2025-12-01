# Visitor - Exportador de Documentos

## O que é o Visitor?

O Visitor permite definir novas operações sobre elementos de uma estrutura sem modificar suas classes. Separa algoritmos dos objetos sobre os quais operam.

## Implementação
![](../../assets/img/visitor.png)
### Elementos do Documento
- **Texto**: Bloco de texto simples
- **Imagem**: Referência para arquivo de imagem  
- **Tabela**: Dados tabulares

### Visitors (Operações)
- **ExportarHTMLVisitor**: Converte elementos para HTML
- **ExportarMarkdownVisitor**: Converte elementos para Markdown

### Código
```python
from abc import ABC, abstractmethod


# ==============================
# Elementos da Estrutura (Element)
# ==============================
class ElementoDocumento(ABC):
    """Interface base que define o método de aceitação do Visitor."""

    @abstractmethod
    def aceitar(self, visitor):
        """Recebe um objeto Visitor e delega a execução para o método adequado."""
        pass


# ------------------------------
# Elementos Concretos
# ------------------------------
class Texto(ElementoDocumento):
    """Elemento que representa um bloco de texto."""

    def __init__(self, conteudo: str):
        self.conteudo = conteudo

    def aceitar(self, visitor):
        # Encaminha o processamento para o método específico do Visitor
        return visitor.visitar_texto(self)


class Imagem(ElementoDocumento):
    """Elemento que representa uma imagem."""

    def __init__(self, caminho: str):
        self.caminho = caminho

    def aceitar(self, visitor):
        return visitor.visitar_imagem(self)


class Tabela(ElementoDocumento):
    """Elemento que representa uma tabela simples."""

    def __init__(self, dados: list[list[str]]):
        self.dados = dados

    def aceitar(self, visitor):
        return visitor.visitar_tabela(self)


# ==========================
# Visitor (interface base)
# ==========================
class VisitorDocumento(ABC):
    """Define a interface para operações realizadas sobre cada tipo de elemento."""

    @abstractmethod
    def visitar_texto(self, texto: Texto):
        pass

    @abstractmethod
    def visitar_imagem(self, imagem: Imagem):
        pass

    @abstractmethod
    def visitar_tabela(self, tabela: Tabela):
        pass


# ==========================
# Visitors Concretos
# ==========================
class ExportarHTMLVisitor(VisitorDocumento):
    """Visitor responsável por exportar elementos para HTML."""

    def visitar_texto(self, texto: Texto):
        return f"<p>{texto.conteudo}</p>"

    def visitar_imagem(self, imagem: Imagem):
        return f'<img src="{imagem.caminho}" />'

    def visitar_tabela(self, tabela: Tabela):
        linhas_html = "".join(
            f"<tr>{''.join(f'<td>{celula}</td>' for celula in linha)}</tr>"
            for linha in tabela.dados
        )
        return f"<table>{linhas_html}</table>"


class ExportarMarkdownVisitor(VisitorDocumento):
    """Visitor responsável por exportar elementos para Markdown."""

    def visitar_texto(self, texto: Texto):
        return texto.conteudo

    def visitar_imagem(self, imagem: Imagem):
        return f"![imagem]({imagem.caminho})"

    def visitar_tabela(self, tabela: Tabela):
        cabecalho = " | ".join(tabela.dados[0])
        separadores = " | ".join("---" for _ in tabela.dados[0])
        linhas = [
            " | ".join(linha) for linha in tabela.dados[1:]
        ]
        return "\n".join([cabecalho, separadores, *linhas])


# ==========================
# Exemplo de Uso
# ==========================
if __name__ == "__main__":
    elementos = [
        Texto("Olá, mundo!"),
        Imagem("/imagens/foto.png"),
        Tabela([
            ["Nome", "Idade"],
            ["Ana", "25"],
            ["Bruno", "30"],
        ])
    ]

    html_visitor = ExportarHTMLVisitor()
    md_visitor = ExportarMarkdownVisitor()

    print("=== Exportação HTML ===")
    for e in elementos:
        print(e.aceitar(html_visitor))

    print("\n=== Exportação Markdown ===")
    for e in elementos:
        print(e.aceitar(md_visitor))

```

## Como Executar

```python
python exemplo_visitor.py
```

## Saída
```
=== Exportação HTML ===
<p>Olá, mundo!</p>
<img src="/imagens/foto.png" />
<table><tr><td>Nome</td><td>Idade</td></tr><tr><td>Ana</td><td>25</td></tr><tr><td>Bruno</td><td>30</td></tr></table>

=== Exportação Markdown ===
Olá, mundo!
![imagem](/imagens/foto.png)
Nome | Idade
--- | ---
Ana | 25
Bruno | 30
```

## Vantagens
- Adiciona operações sem modificar elementos
- Centraliza lógica relacionada em uma classe
- Facilita manutenção de algoritmos complexos