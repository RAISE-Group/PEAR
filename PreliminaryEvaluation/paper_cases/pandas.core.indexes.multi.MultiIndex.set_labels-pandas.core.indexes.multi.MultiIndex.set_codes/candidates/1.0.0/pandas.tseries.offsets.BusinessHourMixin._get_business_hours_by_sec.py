def _get_business_hours_by_sec(self, start, end):
    """
        Return business hours in a day by seconds.
        """
    dtstart = datetime(2014, 4, 1, start.hour, start.minute)
    day = 1 if start < end else 2
    until = datetime(2014, 4, day, end.hour, end.minute)
    return int((until - dtstart).total_seconds())