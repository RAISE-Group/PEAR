@pytest.mark.parametrize('names', [(None, None, None), ('Egon', 'Venkman', None), ('NCC1701D', 'NCC1701D', 'NCC1701D')])
def test_td64arr_mul_int_series(self, box_df_fail, names):
    box = box_df_fail
    exname = names[2] if box is not tm.to_array else names[1]
    tdi = TimedeltaIndex(['0days', '1day', '2days', '3days', '4days'], name=names[0])
    ser = Series([0, 1, 2, 3, 4], dtype=np.int64, name=names[1])
    expected = Series(['0days', '1day', '4days', '9days', '16days'], dtype='timedelta64[ns]', name=exname)
    tdi = tm.box_expected(tdi, box)
    box = Series if box is pd.Index or box is tm.to_array else box
    expected = tm.box_expected(expected, box)
    result = ser * tdi
    tm.assert_equal(result, expected)
    result = ser.__rmul__(tdi)
    tm.assert_equal(result, expected)