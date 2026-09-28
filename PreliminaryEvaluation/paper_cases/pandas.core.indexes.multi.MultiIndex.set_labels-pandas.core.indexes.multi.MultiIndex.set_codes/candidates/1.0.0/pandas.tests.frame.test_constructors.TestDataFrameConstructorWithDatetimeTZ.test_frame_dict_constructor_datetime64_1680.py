def test_frame_dict_constructor_datetime64_1680(self):
    dr = date_range('1/1/2012', periods=10)
    s = Series(dr, index=dr)
    DataFrame({'a': 'foo', 'b': s}, index=dr)
    DataFrame({'a': 'foo', 'b': s.values}, index=dr)