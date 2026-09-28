def test_td64arr_floordiv_tdscalar(self, box_with_array, scalar_td):
    td1 = Series([timedelta(minutes=5, seconds=3)] * 3)
    td1.iloc[2] = np.nan
    expected = Series([0, 0, np.nan])
    td1 = tm.box_expected(td1, box_with_array, transpose=False)
    expected = tm.box_expected(expected, box_with_array, transpose=False)
    result = td1 // scalar_td
    tm.assert_equal(result, expected)