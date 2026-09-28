def test_apply_to_timedelta(self):
    timedelta_NaT = to_timedelta('NaT')
    list_of_valid_strings = ['00:00:01', '00:00:02']
    a = to_timedelta(list_of_valid_strings)
    b = Series(list_of_valid_strings).apply(to_timedelta)
    list_of_strings = ['00:00:01', np.nan, NaT, timedelta_NaT]
    a = to_timedelta(list_of_strings)
    b = Series(list_of_strings).apply(to_timedelta)