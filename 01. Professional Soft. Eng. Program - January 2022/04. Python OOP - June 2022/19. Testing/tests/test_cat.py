"""
2.	Test Cat

Create a class CatTests
In judge you need to submit just the CatTests class, with the unittest module imported.

Create the following tests:
•	Cat's size is increased after eating
•	Cat is fed after eating
•	Cat cannot eat if already fed, raises an error
•	Cat cannot fall asleep if not fed, raises an error
•	Cat is not sleepy after sleeping
"""

import unittest
from unittest import TestCase

from apps.cat import Cat

'''
•	Cat's size is increased after eating
•	Cat is fed after eating
•	Cat cannot eat if already fed, raises an error
•	Cat cannot fall asleep if not fed, raises an error
•	Cat is not sleepy after sleeping
'''


class CatTests(TestCase):
    NAME = 'Pepelyashka'

    def setUp(self) -> None:
        self.cat = Cat(self.NAME)

    def test_eat__expect_size_to_increment(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_eat__expect_fed_to_be_true(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_eat__when_fed_is_true_expect_to_raise(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))
        self.assertIsNotNone(ex)

    def test_sleep__when_fed_is_false__expect_to_raise(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))
        self.assertIsNotNone(ex)

    def test_sleep__expect_sleepy_to_be_false(self):
        # Arrange
        self.cat.eat()

        # Act
        self.cat.sleep()

        # Assert
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()