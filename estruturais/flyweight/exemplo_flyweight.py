"""
Exemplo do padrão Flyweight aplicado a um jogo com múltiplos soldados.
"""

from typing import Dict


class SoldierType:
    """
    O Flyweight (estado intrínseco).
    Armazena dados pesados e imutáveis compartilhados por muitos objetos.
    Ex.: modelo 3D, texturas, sons, animações.
    """

    def __init__(self, name: str, weapon: str, texture: str):
        self.name = name              # Nome da classe do soldado (ex: "Infantaria")
        self.weapon = weapon          # Arma padrão
        self.texture = texture        # Arquivo de textura (grande e compartilhado)

    def render(self, x: int, y: int) -> None:
        """
        Simula o desenho do soldado na posição X,Y.
        Recebe estado extrínseco (coordenadas), pois não deve armazená-lo.
        """
        print(
            f"[Renderizando] {self.name} com arma {self.weapon} "
            f"usando textura '{self.texture}' na posição ({x}, {y})"
        )


class SoldierFactory:
    """
    Flyweight Factory.
    Cria e gerencia instâncias de SoldierType, garantindo reutilização.
    """

    _soldier_types: Dict[str, SoldierType] = {}

    @classmethod
    def get_soldier_type(cls, name: str, weapon: str, texture: str) -> SoldierType:
        """
        Retorna um Flyweight existente ou cria um novo.
        A chave é construída com os atributos intrínsecos.
        """
        key = f"{name}_{weapon}_{texture}"

        # Reuso: se já existe, retorna o existente
        if key not in cls._soldier_types:
            cls._soldier_types[key] = SoldierType(name, weapon, texture)

        return cls._soldier_types[key]


class Soldier:
    """
    Objeto que contém **estado extrínseco** (não compartilhado):
    posição, vida, velocidade etc.
    Mantém uma referência ao Flyweight (estado intrínseco).
    """

    def __init__(self, x: int, y: int, soldier_type: SoldierType):
        self.x = x
        self.y = y
        self.soldier_type = soldier_type

    def draw(self) -> None:
        """
        Desenha o soldado. Apenas repassa o estado extrínseco.
        """
        self.soldier_type.render(self.x, self.y)


# ------------------ Exemplo de Uso ------------------

if __name__ == "__main__":
    # Criando tipos compartilhados (Flyweights)
    infantry_type = SoldierFactory.get_soldier_type(
        "Infantaria", "Rifle", "infantry_texture.png"
    )
    sniper_type = SoldierFactory.get_soldier_type(
        "Sniper", "Sniper Rifle", "sniper_texture.png"
    )

    # Criando soldados com estado extrínseco único
    soldiers = [
        Soldier(10, 20, infantry_type),
        Soldier(15, 25, infantry_type),
        Soldier(20, 30, sniper_type),
    ]

    # Desenhando soldados
    for s in soldiers:
        s.draw()
