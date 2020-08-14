from unittest import TestCase

from src.tape import Tape


class TapeTest(TestCase):
    def setUp(self):
        self.tape = Tape()

    def test_tape_initialized_with_blank_symbol(self):
        self.assertIsNotNone(self.tape.current_square)
        self.assertEqual(" ", self.tape.current_square.symbol)

    def test_tape_initialized_with_single_square(self):
        self.assertIsNone(self.tape.current_square.previous)
        self.assertIsNone(self.tape.current_square.next)

    def test_print_symbol_read_symbol(self):
        self.tape.print_symbol("a")
        self.assertEqual("a", self.tape.current_square.symbol)
        self.assertEqual("a", self.tape.read_current_symbol())

    def test_seek_left_returns_head_on_head(self):
        self.tape.print_symbol("@")
        self.tape.seek_left()
        self.assertEqual("@", self.tape.read_current_symbol())

    def test_seek_right_sets_current_square_new_blank_square_if_next_is_none(self):
        self.tape.print_symbol("1")
        self.tape.seek_right()
        self.assertEqual("", self.tape.read_current_symbol())

    def test_print_symbol_seek_right_print_symbol_seek_left_seek_right(self):
        self.tape.print_symbol("@")
        self.tape.seek_right()
        self.tape.print_symbol("1")
        self.tape.seek_left()
        self.assertEqual("@", self.tape.read_current_symbol())
        self.tape.seek_right()
        self.assertEqual("1", self.tape.read_current_symbol())

    def test_erase(self):
        self.tape.print_symbol("@")
        self.tape.erase()
        self.assertEqual(" ", self.tape.read_current_symbol())

    def test_print_tape_prints_tape_and_seeks_back_to_original_position(self):
        self.tape.print_symbol("@")
        self.tape.seek_right()
        self.tape.print_symbol("1")
        self.tape.seek_right()
        self.tape.seek_right()
        self.tape.print_symbol("0")
        self.tape.seek_right()
        self.tape.seek_right()
        self.tape.print_symbol("1")
        self.tape.seek_left()
        self.tape.print_symbol("e")
        self.tape.seek_left()
        self.assertEqual(3, self.tape.position)
        self.assertEqual("@1 0e1", self.tape.get_state())
        self.assertEqual(3, self.tape.position)
        self.assertEqual("0", self.tape.read_current_symbol())
