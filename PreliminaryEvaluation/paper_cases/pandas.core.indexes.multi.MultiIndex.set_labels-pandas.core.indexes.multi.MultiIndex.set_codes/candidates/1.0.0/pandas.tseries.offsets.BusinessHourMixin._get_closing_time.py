def _get_closing_time(self, dt):
    """
        Get the closing time of a business hour interval by its opening time.

        Parameters
        ----------
        dt : datetime
            Opening time of a business hour interval.

        Returns
        -------
        result : datetime
            Corresponding closing time.
        """
    for i, st in enumerate(self.start):
        if st.hour == dt.hour and st.minute == dt.minute:
            return dt + timedelta(seconds=self._get_business_hours_by_sec(st, self.end[i]))
    assert False