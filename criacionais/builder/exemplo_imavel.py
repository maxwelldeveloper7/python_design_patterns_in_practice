# ======================================================================
# OBJETO COMPLEXO A SER CRIADO
# Representa um imóvel com diversos atributos opcionais.
# ======================================================================

class Imovel:
    def __init__(self, tipo, endereco, quartos, banheiros, garagem, area):
        self.tipo = tipo
        self.endereco = endereco
        self.quartos = quartos
        self.banheiros = banheiros
        self.garagem = garagem
        self.area = area

    def __str__(self):
        """Retorno legível para debug e logs."""
        return (
            f"Imóvel: {self.tipo}, "
            f"Endereço: {self.endereco}, "
            f"{self.quartos} quartos, "
            f"{self.banheiros} banheiros, "
            f"Garagem: {self.garagem}, "
            f"Área: {self.area}m²"
        )


# ======================================================================
# BUILDER
# Responsável por construir o objeto passo a passo.
# Cada método retorna 'self' permitindo método-encadeado (fluent interface).
# ======================================================================

class ImovelBuilder:
    def __init__(self):
        # Valores padrão garantem um estado inicial seguro.
        self._tipo = "Indefinido"
        self._endereco = ""
        self._quartos = 0
        self._banheiros = 0
        self._garagem = False
        self._area = 0

    # ------------------------------------------------------------------
    # Métodos setters com retornos encadeáveis (clean and expressive).
    # ------------------------------------------------------------------

    def com_tipo(self, tipo: str):
        self._tipo = tipo
        return self

    def no_endereco(self, endereco: str):
        self._endereco = endereco
        return self

    def com_quartos(self, quantidade: int):
        self._quartos = quantidade
        return self

    def com_banheiros(self, quantidade: int):
        self._banheiros = quantidade
        return self

    def com_garagem(self, possui: bool = True):
        self._garagem = possui
        return self

    def com_area(self, metros: float):
        self._area = metros
        return self

    # ------------------------------------------------------------------
    # Método final de construção
    # Retorna um objeto Imovel já configurado.
    # ------------------------------------------------------------------
    def build(self) -> Imovel:
        return Imovel(
            tipo=self._tipo,
            endereco=self._endereco,
            quartos=self._quartos,
            banheiros=self._banheiros,
            garagem=self._garagem,
            area=self._area,
        )


# ======================================================================
# DIRETOR (opcional)
# Define construções padronizadas para o Builder.
# Muito útil quando queremos presets, perfis prontos ou rotinas internas.
# ======================================================================

class DiretorImoveis:
    @staticmethod
    def construir_casa_popular(builder: ImovelBuilder) -> Imovel:
        return (
            builder
            .com_tipo("Casa")
            .no_endereco("Rua padrão, nº 100")
            .com_quartos(2)
            .com_banheiros(1)
            .com_garagem(False)
            .com_area(48)
        ).build()

    @staticmethod
    def construir_casa_luxo(builder: ImovelBuilder) -> Imovel:
        return (
            builder
            .com_tipo("Casa de Alto Padrão")
            .no_endereco("Av. Central, nº 500")
            .com_quartos(5)
            .com_banheiros(4)
            .com_garagem(True)
            .com_area(320)
        ).build()


# ======================================================================
# USO PRÁTICO
# O Builder permite montar o objeto passo a passo ou reutilizar padrões do diretor.
# ======================================================================

if __name__ == "__main__":
    # Construção manual com fluent interface
    imovel1 = (
        ImovelBuilder()
        .com_tipo("Apartamento")
        .no_endereco("Rua das Flores, 231")
        .com_quartos(3)
        .com_banheiros(2)
        .com_garagem()
        .com_area(85)
        .build()
    )

    # Construção usando o Diretor
    imovel2 = DiretorImoveis.construir_casa_popular(ImovelBuilder())

    print(imovel1)
    print(imovel2)
