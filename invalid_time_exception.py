class InvalidTimeException(Exception):
    """Exception for invalid time
    """
    def __init__(self):
        self.message = "Entered time is invalid"
        super().__init__(self.message)
