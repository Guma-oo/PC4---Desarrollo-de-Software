from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, pets: list) -> list: pass

class SortByNameStrategy(SortStrategy):
    def sort(self, pets: list) -> list:
        return sorted(pets, key=lambda p: p.name.lower())

class SortBySpeciesStrategy(SortStrategy):
    def sort(self, pets: list) -> list:
        return sorted(pets, key=lambda p: p.species.lower())

class PetSorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def execute_sort(self, pets: list) -> list:
        return self.strategy.sort(pets)