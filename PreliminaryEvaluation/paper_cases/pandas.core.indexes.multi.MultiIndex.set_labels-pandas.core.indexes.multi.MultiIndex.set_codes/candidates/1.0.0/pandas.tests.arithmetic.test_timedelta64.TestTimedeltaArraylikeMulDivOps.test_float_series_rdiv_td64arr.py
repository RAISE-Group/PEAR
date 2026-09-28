@pytest.mark.parametrize('names', [(None, None, None), ('Egon', 'Venkman', None), ('NCC1701D', 'NCC1701D', 'NCC1701D')])
def test_float_series_rdiv_td64arr(self, box_with_array, names):
    box = box_with_array
    tdi = TimedeltaIndex(['0days', '1day', '2days', '3days', '4days'], name=names[0])
    ser = Series([1.5, 3, 4.5, 6, 7.5], dtype=np.float64, name=names[1])
    xname = names[2] if box is not tm.to_array else names[1]
    expected = Series([tdi[n] / ser[n] for n in range(len(ser))], dtype='timedelta64[ns]', name=xname)
    xbox = box
    if box in [pd.Index, tm.to_array] and type(ser) is Series:
        xbox = Series
    tdi = tm.box_expected(tdi, box)
    expected = tm.box_expected(expected, xbox)
    result = ser.__rdiv__(tdi)
    if box is pd.DataFrame:
        assert result is NotImplemented
    else:
        tm.assert_equal(result, expected)