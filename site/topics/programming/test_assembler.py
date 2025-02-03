import unittest

from assembler import program_string_to_list_of_instructions

class TestAssembler(unittest.TestCase):

    def test_program_string_to_list_of_instructions_general_case_returns_instruction_list(self):
        cases = [
            "",
            "hello",
            "hello\nworld",
            "hello world\nthis\nis a\nsuper awesome test",
        ]
        expecteds = [
            [""],
            ["hello"],
            ["hello", "world"],
            ["hello world", "this", "is a", "super awesome test"],
        ]
        for (case, expected) in zip(cases, expecteds):
            with self.subTest(case=case, expected=expected):
                self.assertListEqual(expected, program_string_to_list_of_instructions(case))

    def test_program_string_to_list_of_instructions_white_space_on_ends_returns_instruction_list(self):
        cases = [
            "\n\n\n\n",
            "\nhello",
            "hello\nworld\n",
            "\nhello world\nthis\nis a\nsuper awesome test\n",
            "\n\nhello\n\n\n\nworld\n\n",
        ]
        expecteds = [
            [""],
            ["hello"],
            ["hello", "world"],
            ["hello world", "this", "is a", "super awesome test"],
            ["hello","","","","world"],
        ]
        for (case, expected) in zip(cases, expecteds):
            with self.subTest(case=case, expected=expected):
                self.assertListEqual(expected, program_string_to_list_of_instructions(case))

    def test_program_string_to_list_of_instructions_less_than_16_returns_instruction_list(self):
        cases = [
            "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\nA\nB\nC\nD\nE",
            "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\nA\nB\nC\nD\nE\nF",
        ]
        expecteds = [
            ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E"],
            ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"],
        ]
        for (case, expected) in zip(cases, expecteds):
            with self.subTest(case=case, expected=expected):
                self.assertListEqual(expected, program_string_to_list_of_instructions(case))

    def test_program_string_to_list_of_instructions_greater_than_or_equal_to_16_raises_value_error(self):
        cases = [
            "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\nA\nB\nC\nD\nE\nF\n10",
            "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\nA\nB\nC\nD\nE\nF\n10\n11",
        ]
        for case in cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    program_string_to_list_of_instructions(case)