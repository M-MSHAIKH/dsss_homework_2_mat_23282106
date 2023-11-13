import unittest
from math_quiz import min_max, arithmatic_operations, calculations


class TestMathGame(unittest.TestCase):

    def test_min_max(self):
        # Test if the random numbers generated is within the specified range, set by the user
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = min_max(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def tes_arithmatic_operations(self):
        # This function test whether generated sign is valid
        valid_signs = ['+', '-', '*']
        for _ in range(len(valid_signs)):
            result = choose_sign()
            self.assertIn(result, valid_signs, f"The result '{result}' is not a valid mathematical sign")
            pass



    def test_calculations(self):
        # This funcation check validity of the Arithmatic Operation

            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 5, '*', '8 * 5', 40),
                (2, 1, '-', '5 - 7', 1),
                (8, 8, '-', '8 - 8', 0),
                (6, 5, '-', '6 + 5', 11)
            ]


            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                PROBLEM, ANSWER = apply_operation(num1,num2,operator)
                self.assertEqual(expected_problem,PROBLEM, f"The expected problem don't match the problem. Expected Problem: {expected_problem}, Problem: {PROBLEM}")
                self.assertEqual(expected_answer,ANSWER, f"The expected problem don't match the problem. Expected Answer: {expected_answer}, Answer: {ANSWER}")
                pass



if __name__ == "__main__":
    unittest.main()

