def test_constructor_dict_timedelta_index(self):
    expected = Series(data=['A', 'B', 'C'], index=pd.to_timedelta([0, 10, 20], unit='s'))
    result = Series(data={pd.to_timedelta(0, unit='s'): 'A', pd.to_timedelta(10, unit='s'): 'B', pd.to_timedelta(20, unit='s'): 'C'}, index=pd.to_timedelta([0, 10, 20], unit='s'))
    tm.assert_series_equal(result, expected)