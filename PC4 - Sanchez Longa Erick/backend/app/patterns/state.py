from abc import ABC, abstractmethod

class PetState(ABC):
    @abstractmethod
    def next_state(self) -> str: pass

class PerdidaState(PetState):
    def next_state(self) -> str: return "En Resguardo"

class EnResguardoState(PetState):
    def next_state(self) -> str: return "Reunida"

class ReunidaState(PetState):
    def next_state(self) -> str: return "Reunida"

class PetStateContext:
    def __init__(self, current_status: str):
        states = {
            "Perdida": PerdidaState(),
            "En Resguardo": EnResguardoState(),
            "Reunida": ReunidaState()
        }
        self.state = states.get(current_status, PerdidaState())

    def advance_state(self) -> str:
        return self.state.next_state()