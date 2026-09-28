@property
def time(self):
    """
        Returns numpy array of datetime.time. The time part of the Timestamps.
        """
    if self.tz is not None and (not timezones.is_utc(self.tz)):
        timestamps = self._local_timestamps()
    else:
        timestamps = self.asi8
    return tslib.ints_to_pydatetime(timestamps, box='time')