def test_setitem_cast(self, float_frame):
    float_frame['D'] = float_frame['D'].astype('i8')
    assert float_frame['D'].dtype == np.int64
    float_frame['B'] = 0
    assert float_frame['B'].dtype == np.int64
    float_frame['B'] = np.arange(len(float_frame))
    assert issubclass(float_frame['B'].dtype.type, np.integer)
    float_frame['foo'] = 'bar'
    float_frame['foo'] = 0
    assert float_frame['foo'].dtype == np.int64
    float_frame['foo'] = 'bar'
    float_frame['foo'] = 2.5
    assert float_frame['foo'].dtype == np.float64
    float_frame['something'] = 0
    assert float_frame['something'].dtype == np.int64
    float_frame['something'] = 2
    assert float_frame['something'].dtype == np.int64
    float_frame['something'] = 2.5
    assert float_frame['something'].dtype == np.float64
    df = DataFrame(np.random.rand(30, 3), columns=tuple('ABC'))
    df['event'] = np.nan
    df.loc[10, 'event'] = 'foo'
    result = df.dtypes
    expected = Series([np.dtype('float64')] * 3 + [np.dtype('object')], index=['A', 'B', 'C', 'event'])
    tm.assert_series_equal(result, expected)
    df = DataFrame({'one': np.arange(6, dtype=np.int8)})
    df.loc[1, 'one'] = 6
    assert df.dtypes.one == np.dtype(np.int8)
    df.one = np.int8(7)
    assert df.dtypes.one == np.dtype(np.int8)