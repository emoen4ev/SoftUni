"""
1.	Test Worker

Load provided skeleton in the IDE you use.
Add new project Tests.
Create a class WorkerTests
In judge you need to submit just the WokerTests class, with the unittest module imported.
Create the following tests:
•	Test if the worker is initialized with the correct name, salary, and energy
•	Test if the worker's energy is incremented after the rest method is called
•	Test if an error is raised if the worker tries to work with negative energy or equal to 0
•	Test if the worker's money is increased by his salary correctly after the work method is called
•	Test if the worker's energy is decreased after the work method is called
•	Test if the get_info method returns the proper string with correct values
"""

import unittest
from unittest import TestCase

from apps.worker import Worker


class WorkerTests(TestCase):
    NAME = 'Test Worker'
    SALARY = 1024
    # ENERGY = 1
    ENERGY = 2

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test__init__when_valid_props__expect_correct_values(self):
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)
        self.assertEqual(0, self.worker.money)
        # self.assertEqual(Worker.INITIAL_MONEY, self.worker.money)

    def test__rest__expect_energy_to_be_incremented(self):
        self.worker.rest()
        self.assertEqual(self.ENERGY + 1, self.worker.energy)

        # Act   Arrange           Assert

    def test__work__when_energy_is_0_or_negative__expect_to_raise(self):
        worker_1 = Worker(self.NAME, self.SALARY, 0)

        with self.assertRaises(Exception) as ex_1:
            worker_1.work()
        self.assertEqual('Not enough energy.', str(ex_1.exception))

        self.assertIsNotNone(ex_1)

        worker_2 = Worker(self.NAME, self.SALARY, -1)

        with self.assertRaises(Exception) as ex_2:
            worker_2.work()
        self.assertEqual('Not enough energy.', str(ex_2.exception))

        self.assertIsNotNone(ex_2)

    def test__work__when_enough_energy__expect_money_to_be_increased_by_salary(self):
        self.worker.work()
        self.worker.work()

        self.assertEqual(2 * self.SALARY, self.worker.money)
        # self.assertEqual(1 * self.SALARY, self.worker.money)

    def test__work__when_enough_energy__expect_energy_to_decrement(self):
        self.worker.work()

        self.assertEqual(self.ENERGY - 1, self.worker.energy)

    def test__get_info__expect_correct_result(self):
        actual_info = self.worker.get_info()
        expected_info = f'{self.NAME} has saved {self.worker.money} money.'
        # expected_info = f'{self.NAME} has saved {0} money.'

        self.assertEqual(expected_info, actual_info)


if __name__ == '__main__':
    unittest.main()