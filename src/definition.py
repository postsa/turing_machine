from os import path
from json import loads


class Definition:
    def __init__(self, *path_parts):
        config_path = path.join(*path_parts)
        file_data = None
        with open(config_path, "r+") as f:
            file_data = f.read()
        self.config_map = loads(file_data) if file_data else {}

    def get_operations(self, symbol, m_config):
        definition_for_symbol = self.get_definition_for_symbol(m_config, symbol)
        configured_operations = definition_for_symbol["operations"]
        operation_functions = []
        for o in configured_operations:
            if o.startswith("P"):
                symbol_to_print = o.split("|")[-1]
                operation_functions.append(
                    lambda t, v=symbol_to_print: t.print_symbol(v)
                )
            elif o == "E":
                operation_functions.append(lambda t: t.erase())
            elif o == "R":
                operation_functions.append(lambda t: t.seek_right())
            elif o == "L":
                operation_functions.append(lambda t: t.seek_left())

        return operation_functions

    def get_final_m_configuration(self, symbol, m_config):
        definition_for_symbol = self.get_definition_for_symbol(m_config, symbol)
        return definition_for_symbol["final-m-config"]

    def get_definition_for_symbol(self, m_config, symbol):
        current_config_definition = self.config_map.get(m_config, {})
        definition_for_symbol = current_config_definition.get(symbol)
        if not definition_for_symbol:
            definition_for_symbol = current_config_definition["any"]
        return definition_for_symbol
