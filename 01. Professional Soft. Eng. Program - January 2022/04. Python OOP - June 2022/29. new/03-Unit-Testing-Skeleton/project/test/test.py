from project.robot import Robot

from unittest import TestCase


class TestRobot(TestCase):
    def setUp(self):
        self.robot1 = Robot('001', 'Education', 100, 500.0)
        self.robot2 = Robot('002', 'Humanoids', 200, 1000.0)

    def test_category_setter_is_valid(self):
        self.robot1.category = 'Entertainment'
        self.assertEqual(self.robot1.category, 'Entertainment')

    def test_category_setter_is_invalid(self):
        with self.assertRaises(ValueError):
            self.robot1.category = 'Medical'

    def test_price_setter_is_valid(self):
        self.robot1.price = 600.0
        self.assertEqual(self.robot1.price, 600.0)

    def test_price_setter_is_invalid(self):
        with self.assertRaises(ValueError):
            self.robot1.price = -500.0

    def test_upgrade_new_component(self):
        result = self.robot1.upgrade('Laser', 100.0)
        self.assertEqual(result, 'Robot 001 was upgraded with Laser.')
        self.assertEqual(self.robot1.price, 650.0)

    def test_upgrade_existing_component(self):
        self.robot1.upgrade('Laser', 100.0)
        result = self.robot1.upgrade('Laser', 200.0)
        self.assertEqual(result, 'Robot 001 was not upgraded.')
        self.assertEqual(self.robot1.price, 650.0)

    def test_update_is_valid(self):
        result = self.robot1.update(2.0, 50)
        self.assertEqual(result, 'Robot 001 was updated to version 2.0.')
        self.assertEqual(self.robot1.software_updates, [2.0])
        self.assertEqual(self.robot1.available_capacity, 50)

    def test_update_is_invalid_version(self):
        self.robot1.update(2.0, 50)
        result = self.robot1.update(1.0, 50)
        self.assertEqual(result, 'Robot 001 was not updated.')
        self.assertEqual(self.robot1.software_updates, [2.0])
        self.assertEqual(self.robot1.available_capacity, 50)

    def test_update_is_invalid_capacity(self):
        result = self.robot1.update(2.0, 200)
        self.assertEqual(result, 'Robot 001 was not updated.')
        self.assertEqual(self.robot1.software_updates, [])
        self.assertEqual(self.robot1.available_capacity, 100)

    def test_gt_more_expensive(self):
        result = self.robot2 > self.robot1
        self.assertEqual(result, 'Robot with ID 002 is more expensive than Robot with ID 001.')

    def test_gt_equal_price(self):
        result = self.robot1 > self.robot2
        self.assertEqual(result, 'Robot with ID 001 costs equal to Robot with ID 002.')

    def test_gt_cheaper(self):
        result = self.robot1 > self.robot2
        self.assertEqual(result, 'Robot with ID 001 is cheaper than Robot with ID 002.')