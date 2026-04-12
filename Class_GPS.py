class Region:
    def __init__(self, nombre: str, poblacion_total: int, infectados: int, fallecidos: int, nivel_medico: int, fronteras_abiertas: bool):
        self.nombre: str = nombre
        self.poblacion_total: int = poblacion_total
        self.infectados: int = infectados
        self.fallecidos: int = fallecidos
        self.nivel_medico: int = nivel_medico
        self.fronteras_abiertas: bool = fronteras_abiertas

    def  obtener_infectados(self) -> int:
        pass

    def obtener_fallecidos(self) -> int:
        pass

    def obtener_poblacion_viva(self) -> int:
        pass

    def obtener_estado_frontera(self) -> bool:
        pass

    def cerrar_frontera(self) -> None:
        pass

    def iniciar_contagio(self) -> None:
        pass

    def simular_dia(self, infectividad, letalidad) -> None:
        pass


class Jugador:
    def __init__(self, rol: str, puntos: int, infectividad: float, letalidad: float):
        self.rol: str = rol
        self.puntos: int = puntos
        self.infectividad: float = infectividad
        self.letalidad: float = letalidad

class Mundo:
    def __init__(self, dia: int):
        self.dia: int = dia
        self.regiones: list[Region]

    def usar_puntos(self, mundo):
        pass