import random
import pytest

from clock import Clock
from invalid_time_exception import InvalidTimeException


class TestClock:

    @staticmethod
    def __find_angle(hours: int, minutes: int):
        test_clock = Clock(hours, minutes)
        angle = test_clock.find_angle()
        assert 0 <= angle <= 180
        return angle

    def test_find_angle_success(self):
        """Test for valid time
        """
        for _ in range(5):
            hours = random.randint(0, 11)
            minutes = random.randint(0, 59)
            angle = self.__find_angle(hours, minutes)
            print("%02d:%02d = %s degrees" % (hours, minutes, angle))

    def test_find_angle_raises_exception(self):
        """Test for invalid time
        """
        with pytest.raises(InvalidTimeException):
            test_clock = Clock(-2, 4)