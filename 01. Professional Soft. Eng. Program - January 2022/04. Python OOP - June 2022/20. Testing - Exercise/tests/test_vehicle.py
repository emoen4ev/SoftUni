import unittest
from unittest import TestCase

from project.vehicle import Vehicle


class VehicleTests(TestCase):
    FUEL = 100
    HORSE_POWER = 120
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test_vehicle_init(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive__raises_error__when_fuel_is_not_enough(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.drive(100)
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual('Not enough fuel', str(error.exception))

    def test_drive__reduces_fuel__when_distance_is_reachable(self):
        distance = 50
        fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * distance

        self.vehicle.drive(distance)

        expected_result = self.FUEL - fuel_needed
        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_drive__reduces_fuel__with_max_possible_distance(self):
        distance = self.FUEL / self.DEFAULT_FUEL_CONSUMPTION

        self.vehicle.drive(distance)

        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel__raises_error__when_capacity_is_not_enough(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.refuel(self.vehicle.capacity + 1)
        self.assertEqual('Too much fuel', str(error.exception))

    def test_refuel__increases_fuel_in_the_car(self):
        fuel_amount = 20
        self.vehicle.fuel -= fuel_amount

        self.vehicle.refuel(fuel_amount)

        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test_vehicle_str__returns_proper_string_message(self):
        actual_result = str(self.vehicle)
        expected_result = f"The vehicle has {self.HORSE_POWER} " \
                          f"horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()