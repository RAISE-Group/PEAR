@staticmethod
def merge_class(base, other):
    """
        Merge holiday calendars together. The base calendar
        will take precedence to other. The merge will be done
        based on each holiday's name.

        Parameters
        ----------
        base : AbstractHolidayCalendar
          instance/subclass or array of Holiday objects
        other : AbstractHolidayCalendar
          instance/subclass or array of Holiday objects
        """
    try:
        other = other.rules
    except AttributeError:
        pass
    if not isinstance(other, list):
        other = [other]
    other_holidays = {holiday.name: holiday for holiday in other}
    try:
        base = base.rules
    except AttributeError:
        pass
    if not isinstance(base, list):
        base = [base]
    base_holidays = {holiday.name: holiday for holiday in base}
    other_holidays.update(base_holidays)
    return list(other_holidays.values())