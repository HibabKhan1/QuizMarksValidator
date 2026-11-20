import unittest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By


class QuizValidationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        file_path = Path("quiz_validation.html").resolve().as_uri()
        self.driver.get(file_path)

    def test_marks_validation(self):
        test_cases = [
            (-1, "Invalid Marks"),
            (0, "Valid Marks"),
            (5, "Valid Marks"),
            (10, "Valid Marks"),
            (11, "Invalid Marks")
        ]

        for marks, expected in test_cases:
            with self.subTest(marks=marks):
                field = self.driver.find_element(By.ID, "marks")
                field.clear()
                field.send_keys(str(marks))

                self.driver.find_element(
                    By.ID, "validateBtn"
                ).click()

                actual = self.driver.find_element(
                    By.ID, "result"
                ).text

                print(
                    f"Input: {marks}, Expected: {expected}, Actual: {actual}"
                )

                self.assertEqual(actual, expected)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()