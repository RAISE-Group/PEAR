def test_dt64arr_naive_sub_dt64ndarray(self, box_with_array):
    dti = pd.date_range('2016-01-01', periods=3, tz=None)
    dt64vals = dti.values
    dtarr = tm.box_expected(dti, box_with_array)
    expected = dtarr - dtarr
    result = dtarr - dt64vals
    tm.assert_equal(result, expected)
    result = dt64vals - dtarr
    tm.assert_equal(result, expected)