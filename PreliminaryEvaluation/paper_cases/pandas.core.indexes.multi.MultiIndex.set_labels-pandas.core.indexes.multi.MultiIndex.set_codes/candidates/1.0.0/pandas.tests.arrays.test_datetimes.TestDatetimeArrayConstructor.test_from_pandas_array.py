def test_from_pandas_array(self):
    arr = pd.array(np.arange(5, dtype=np.int64)) * 3600 * 10 ** 9
    result = DatetimeArray._from_sequence(arr, freq='infer')
    expected = pd.date_range('1970-01-01', periods=5, freq='H')._data
    tm.assert_datetime_array_equal(result, expected)