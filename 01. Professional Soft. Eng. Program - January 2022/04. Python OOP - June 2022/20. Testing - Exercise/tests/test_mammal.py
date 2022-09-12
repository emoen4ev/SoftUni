from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    NAME = 'Pesho'
    MAMMAL_TYPE = 'TYPE'
    SOUND = 'SOUND'
    KINGDOM = 'animals'

    def setUp(self) -> None:
        self.mammal = Mammal(self.NAME, self.MAMMAL_TYPE, self.SOUND)

    def test_mammal_init__should_create_proper_object(self):
        self.assertEqual(self.NAME, self.mammal.name)
        self.assertEqual(self.MAMMAL_TYPE, self.mammal.type)
        self.assertEqual(self.SOUND, self.mammal.sound)
        self.assertEqual(self.KINGDOM, self.mammal._Mammal__kingdom)

    def test_make_sound__returns_proper_result(self):
        actual_result = self.mammal.make_sound()
        expected_result = f"{self.NAME} makes {self.SOUND}"

        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom__return_animals(self):
        actual_result = self.mammal.get_kingdom()

        self.assertEqual(self.KINGDOM, actual_result)

    def test_info__returns_proper_string(self):
        actual_result = self.mammal.info()
        expected_result = f"{self.NAME} is of type {self.MAMMAL_TYPE}"

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()