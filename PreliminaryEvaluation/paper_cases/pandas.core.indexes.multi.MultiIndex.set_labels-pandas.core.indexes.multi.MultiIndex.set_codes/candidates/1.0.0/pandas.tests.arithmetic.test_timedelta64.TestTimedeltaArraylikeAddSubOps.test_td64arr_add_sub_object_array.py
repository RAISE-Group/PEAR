def test_td64arr_add_sub_object_array(self, box_with_array):
    tdi = pd.timedelta_range('1 day', periods=3, freq='D')
    tdarr = tm.box_expected(tdi, box_with_array)
    other = np.array([pd.Timedelta(days=1), pd.offsets.Day(2), pd.Timestamp('2000-01-04')])
    warn = PerformanceWarning if box_with_array is not pd.DataFrame else None
    with tm.assert_produces_warning(warn):
        result = tdarr + other
    expected = pd.Index([pd.Timedelta(days=2), pd.Timedelta(days=4), pd.Timestamp('2000-01-07')])
    expected = tm.box_expected(expected, box_with_array)
    tm.assert_equal(result, expected)
    with pytest.raises(TypeError):
        with tm.assert_produces_warning(warn):
            tdarr - other
    with tm.assert_produces_warning(warn):
        result = other - tdarr
    expected = pd.Index([pd.Timedelta(0), pd.Timedelta(0), pd.Timestamp('2000-01-01')])
    expected = tm.box_expected(expected, box_with_array)
    tm.assert_equal(result, expected)