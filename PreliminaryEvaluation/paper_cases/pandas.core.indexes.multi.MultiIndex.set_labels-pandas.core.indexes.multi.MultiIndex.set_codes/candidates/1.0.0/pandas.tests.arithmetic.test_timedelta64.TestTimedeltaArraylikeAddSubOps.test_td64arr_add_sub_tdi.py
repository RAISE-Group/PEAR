@pytest.mark.parametrize('names', [(None, None, None), ('Egon', 'Venkman', None), ('NCC1701D', 'NCC1701D', 'NCC1701D')])
def test_td64arr_add_sub_tdi(self, box, names):
    if box is pd.DataFrame and names[1] == 'Venkman':
        pytest.skip('Name propagation for DataFrame does not behave like it does for Index/Series')
    tdi = TimedeltaIndex(['0 days', '1 day'], name=names[0])
    ser = Series([Timedelta(hours=3), Timedelta(hours=4)], name=names[1])
    expected = Series([Timedelta(hours=3), Timedelta(days=1, hours=4)], name=names[2])
    ser = tm.box_expected(ser, box)
    expected = tm.box_expected(expected, box)
    result = tdi + ser
    tm.assert_equal(result, expected)
    if box is not pd.DataFrame:
        assert result.dtype == 'timedelta64[ns]'
    else:
        assert result.dtypes[0] == 'timedelta64[ns]'
    result = ser + tdi
    tm.assert_equal(result, expected)
    if box is not pd.DataFrame:
        assert result.dtype == 'timedelta64[ns]'
    else:
        assert result.dtypes[0] == 'timedelta64[ns]'
    expected = Series([Timedelta(hours=-3), Timedelta(days=1, hours=-4)], name=names[2])
    expected = tm.box_expected(expected, box)
    result = tdi - ser
    tm.assert_equal(result, expected)
    if box is not pd.DataFrame:
        assert result.dtype == 'timedelta64[ns]'
    else:
        assert result.dtypes[0] == 'timedelta64[ns]'
    result = ser - tdi
    tm.assert_equal(result, -expected)
    if box is not pd.DataFrame:
        assert result.dtype == 'timedelta64[ns]'
    else:
        assert result.dtypes[0] == 'timedelta64[ns]'