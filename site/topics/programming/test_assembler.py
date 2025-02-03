import unittest

from assembler import (create_assembled_string,
                       parse_instruction_operator,
                       parse_instruction_operand,
                       program_string_to_list_of_instructions)

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

    def test_parse_instruction_operator_general_case_returns_operator(self):
        cases = [
            ["NOOP"],
            ["LDAR"],
            ["LDAD"],
            ["LDBR"],
            ["LDBD"],
            ["SAVA"],
            ["SAVB"],
            ["ADDB"],
            ["SUBB"],
            ["JMPA"],
            ["NOOP"],
            ["NOOP"],
            ["NOOP"],
            ["OUTU"],
            ["OUTS"],
            ["HALT"],
        ]
        expecteds = [
            0x0,
            0x1,
            0x2,
            0x3,
            0x4,
            0x5,
            0x6,
            0x7,
            0x8,
            0x9,
            0x0,
            0x0,
            0x0,
            0xd,
            0xe,
            0xf,
        ]
        for (case, expected) in zip(cases, expecteds):
            with self.subTest(case=case, expected=expected):
                self.assertEqual(expected, parse_instruction_operator(case))

    def test_parse_instruction_operator_undefined_operator_raises_value_error(self):
        cases = [
            [""],
            ["A"],
            ["TLAH"],
        ]
        for case in cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    parse_instruction_operator(case)

    def test_parse_instruction_operand_instruction_with_no_operand_returns_zero(self):
        cases = [
            ["NOOP"],
            ["ADDB"],
            ["SUBB"],
            ["HALT"],
        ]
        for case in cases:
            with self.subTest(case=case):
                self.assertEqual(0, parse_instruction_operand(case))

    def test_parse_instruction_operand_instruction_with_no_operand_but_operand_provided_raises_value_error(self):
        cases = [
            ["NOOP", 0],
            ["ADDB", 0, 0],
            ["SUBB", 0, 0, 0],
            ["HALT", 0, 0, 0, 0],
        ]
        for case in cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    parse_instruction_operand(case)

    def test_parse_instruction_operand_instruction_with_operand_binary_provided_returns_operand(self):
        cases = [
            ["LDAR", "0b0000"],
            ["LDAD", "0b0001"],
            ["LDBR", "0b0010"],
            ["LDBD", "0b0011"],
            ["SAVA", "0b0100"],
            ["SAVB", "0b0101"],
            ["JMPA", "0b0110"],
            ["OUTU", "0b0111"],
            ["OUTS", "0b1000"],
        ]
        expecteds = [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
        ]
        for (case, expected) in zip(cases, expecteds):
            with self.subTest(case=case, expected=expected):
                self.assertEqual(expected, parse_instruction_operand(case))

    def test_parse_instruction_operand_instruction_with_operand_hex_provided_returns_operand(self):
        cases = [
            ["LDAR", "0xf"],
            ["LDAD", "0xe"],
            ["LDBR", "0xd"],
            ["LDBD", "0xc"],
            ["SAVA", "0xb"],
            ["SAVB", "0xa"],
            ["JMPA", "0x9"],
            ["OUTU", "0x8"],
            ["OUTS", "0x7"],
        ]
        expecteds = [
            15,
            14,
            13,
            12,
            11,
            10,
            9,
            8,
            7,
        ]
        for (case, expected) in zip(cases, expecteds):
            with self.subTest(case=case, expected=expected):
                self.assertEqual(expected, parse_instruction_operand(case))

    def test_parse_instruction_operand_instruction_with_operand_decimal_provided_returns_operand(self):
        cases = [
            ["LDAR", "0"],
            ["LDAD", "1"],
            ["LDBR", "2"],
            ["LDBD", "3"],
            ["SAVA", "4"],
            ["SAVB", "5"],
            ["JMPA", "6"],
            ["OUTU", "7"],
            ["OUTS", "8"],
        ]
        expecteds = [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
        ]
        for (case, expected) in zip(cases, expecteds):
            with self.subTest(case=case, expected=expected):
                self.assertEqual(expected, parse_instruction_operand(case))

    def test_parse_instruction_operand_instruction_with_operand_not_valid_number_encoding_raises_value_error(self):
        cases = [
            ["LDAR", ""],
            ["LDAD", "a"],
            ["LDBR", "hello"],
            ["LDBD", "0o0"],
        ]
        for case in cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    parse_instruction_operand(case)

    def test_parse_instruction_operand_instruction_with_operand_but_wrong_number_of_operands_raises_value_error(self):
        cases = [
            ["LDAR"],
            ["LDAD", "0", "1"],
            ["LDBR", "0", "1", "2"],
        ]
        for case in cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    parse_instruction_operand(case)

    def test_parse_instruction_operand_instruction_with_operand_value_too_high_raises_value_error(self):
        cases = [
            ["LDAR", "0b10000"],
            ["LDAD", "0b10001"],
            ["LDBR", "0x10"],
            ["LDBD", "0x11"],
            ["SAVA", "16"],
            ["SAVB", "17"],
        ]
        for case in cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    parse_instruction_operand(case)

    def test_create_assembled_string_general_case_returns_assembled_string(self):
        cases = [
            [],
            [0x00],
            [0x00,0x11,0x22,0x33,0x44,0x55,0x66,0x77,0x88,0x99,0xaa,0xbb,0xcc,0xdd,0xee,0xff],
        ]
        expecteds = [
            "v2.0 raw\n",
            "v2.0 raw\n0x00\n",
            "v2.0 raw\n0x00\n0x11\n0x22\n0x33\n0x44\n0x55\n0x66\n0x77\n0x88\n0x99\n0xaa\n0xbb\n0xcc\n0xdd\n0xee\n0xff\n",
        ]
        for (case, expected) in zip(cases, expecteds):
            with self.subTest(case=case, expected=expected):
                self.assertEqual(expected, create_assembled_string(case))

    def test_create_assembled_string_leading_zero_operator_adds_leading_zero_to_instructions(self):
        case = [0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b,0x0c,0x0d,0x0e,0x0f]
        expected = "v2.0 raw\n0x00\n0x01\n0x02\n0x03\n0x04\n0x05\n0x06\n0x07\n0x08\n0x09\n0x0a\n0x0b\n0x0c\n0x0d\n0x0e\n0x0f\n"
        self.assertEqual(expected, create_assembled_string(case))