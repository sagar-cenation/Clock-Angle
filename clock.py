import logging

from invalid_time_exception import InvalidTimeException


class Clock:
    def __init__(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes
        self.validate_clock()

    def validate_clock(self):
        if not(0 <= self.hours < 12) or not (0 <= self.minutes < 60):
            raise InvalidTimeException

    def find_angle(self):
        """Calculates the angle between hour and minute hands
        """
        logging.info("Calculating angle for %s hours and %s minutes", self.hours, self.minutes)

        hour_pos = ((self.hours * 360) / 12) + ((self.minutes * 360) / (12*60))
        minute_pos = (self.minutes * 360) / 60

        angle = abs(hour_pos - minute_pos)

        # If the angle is greater than 180, calculate the smaller angle
        if angle > 180:
            angle = 360 - angle

        logging.info("Angle calculated successfully")
        return angle
