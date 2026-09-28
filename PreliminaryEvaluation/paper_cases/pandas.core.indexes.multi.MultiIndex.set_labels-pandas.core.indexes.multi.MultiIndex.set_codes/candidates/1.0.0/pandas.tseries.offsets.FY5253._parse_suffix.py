@classmethod
def _parse_suffix(cls, varion_code, startingMonth_code, weekday_code):
    if varion_code == 'N':
        variation = 'nearest'
    elif varion_code == 'L':
        variation = 'last'
    else:
        raise ValueError(f'Unable to parse varion_code: {varion_code}')
    startingMonth = ccalendar.MONTH_TO_CAL_NUM[startingMonth_code]
    weekday = ccalendar.weekday_to_int[weekday_code]
    return {'weekday': weekday, 'startingMonth': startingMonth, 'variation': variation}