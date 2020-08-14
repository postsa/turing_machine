from os import getcwd, system

import sys
from time import sleep

from src.definition import Definition
from src.machine import Machine


def compute_current_value(state):
    binary_string = "."
    for char in state:
        if char == "0" or char == "1":
            binary_string += char
    return parse_bin(binary_string)


def parse_bin(s):
    return int(s[1:], 2) / 2.0 ** (len(s) - 1)


if __name__ == "__main__":
    instructions = sys.argv[1]

    definition = Definition(getcwd(), "src", "config", f"{instructions}.json")
    machine = Machine(definition, "b")
    system("clear")
    i = 0
    while i < 1000:
        state = machine.next()
        position = machine.tape.position
        position_string = " "
        while position > 1:
            position_string += " "
            position -= 1
        position_string += "^"
        print(state)
        print(position_string)
        print(f"current state: {machine.m_configuration}")
        print(f"current value: {compute_current_value(state)}")
        i += 1
        sleep(0.25)
        system("clear")
