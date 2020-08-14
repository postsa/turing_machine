from src.tape import Tape


class Machine:
    def __init__(self, definition, initial_m_config):
        self.definition = definition
        self.tape = Tape()
        self.m_configuration = initial_m_config

    def operate(self):
        symbol = self.tape.read_current_symbol()
        operations = self.definition.get_operations(symbol, self.m_configuration)
        for o in operations:
            o(self.tape)
        self.m_configuration = self.definition.get_final_m_configuration(
            symbol, self.m_configuration
        )

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        self.operate()
        return self.tape.get_state()
