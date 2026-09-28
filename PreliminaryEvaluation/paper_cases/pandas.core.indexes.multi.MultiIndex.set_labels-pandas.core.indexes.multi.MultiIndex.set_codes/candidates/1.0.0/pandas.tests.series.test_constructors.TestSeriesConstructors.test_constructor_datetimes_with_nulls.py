def test_constructor_datetimes_with_nulls(self):
    for arr in [np.array([None, None, None, None, datetime.now(), None]), np.array([None, None, datetime.now(), None])]:
        result = Series(arr)
        assert result.dtype == 'M8[ns]'