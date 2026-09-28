def test_dt64arr_aware_sub_dt64ndarray_raises(self, tz_aware_fixture, box_with_array):
    tz = tz_aware_fixture
    dti = pd.date_range('2016-01-01', periods=3, tz=tz)
    dt64vals = dti.values
    dtarr = tm.box_expected(dti, box_with_array)
    msg = 'subtraction must have the same timezones or'
    with pytest.raises(TypeError, match=msg):
        dtarr - dt64vals
    with pytest.raises(TypeError, match=msg):
        dt64vals - dtarr