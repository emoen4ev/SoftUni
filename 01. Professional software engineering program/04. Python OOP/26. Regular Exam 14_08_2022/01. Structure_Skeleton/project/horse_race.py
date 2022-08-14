class HorseRace:
    VALID_TYPES = ["Winter", "Spring", "Autumn", "Summer"]

    def __init__(self, race_type: str, jockeys: list):
        self.race_type = race_type
        self.jockeys = jockeys

        @property
        def race_type(self):
            return self.__race_type

        @race_type.setter
        def race_type(self, value):
            if value not in self.VALID_TYPES:
                raise ValueError(f'Race type does not exist!')
            self.__race_type = value