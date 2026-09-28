def test_from_records_with_datetimes(self):
    if not is_platform_little_endian():
        pytest.skip('known failure of test on non-little endian')
    expected = DataFrame({'EXPIRY': [datetime(2005, 3, 1, 0, 0), None]})
    arrdata = [np.array([datetime(2005, 3, 1, 0, 0), None])]
    dtypes = [('EXPIRY', '<M8[ns]')]
    try:
        recarray = np.core.records.fromarrays(arrdata, dtype=dtypes)
    except ValueError:
        pytest.skip('known failure of numpy rec array creation')
    result = DataFrame.from_records(recarray)
    tm.assert_frame_equal(result, expected)
    arrdata = [np.array([datetime(2005, 3, 1, 0, 0), None])]
    dtypes = [('EXPIRY', '<M8[m]')]
    recarray = np.core.records.fromarrays(arrdata, dtype=dtypes)
    result = DataFrame.from_records(recarray)
    tm.assert_frame_equal(result, expected)