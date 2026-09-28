def test_datetime_date_tuple_columns_from_dict(self):
    v = date.today()
    tup = (v, v)
    result = DataFrame({tup: Series(range(3), index=range(3))}, columns=[tup])
    expected = DataFrame([0, 1, 2], columns=pd.Index(pd.Series([tup])))
    tm.assert_frame_equal(result, expected)