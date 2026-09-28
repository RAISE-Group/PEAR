def _get_roll(self, i, before_day_of_month, after_day_of_month):
    """
        Return an array with the correct n for each date in i.

        The roll array is based on the fact that i gets rolled back to
        the first day of the month.
        """
    raise AbstractMethodError(self)