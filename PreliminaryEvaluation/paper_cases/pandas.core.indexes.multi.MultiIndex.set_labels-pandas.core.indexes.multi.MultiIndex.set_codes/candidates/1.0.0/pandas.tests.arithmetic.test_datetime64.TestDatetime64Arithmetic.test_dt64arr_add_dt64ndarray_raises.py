def test_dt64arr_add_dt64ndarray_raises(self, tz_naive_fixture, box_with_array):
    tz = tz_naive_fixture
    dti = pd.date_range('2016-01-01', periods=3, tz=tz)
    dt64vals = dti.values
    dtarr = tm.box_expected(dti, box_with_array)
    msg = 'cannot add'
    with pytest.raises(TypeError, match=msg):
        dtarr + dt64vals
    with pytest.raises(TypeError, match=msg):
        dt64vals + dtarr