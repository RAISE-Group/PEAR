def test_setitem_ndarray_1d(self):
    df = DataFrame(index=Index(np.arange(1, 11)))
    df['foo'] = np.zeros(10, dtype=np.float64)
    df['bar'] = np.zeros(10, dtype=np.complex)
    with pytest.raises(ValueError):
        df.loc[df.index[2:5], 'bar'] = np.array([2.33j, 1.23 + 0.1j, 2.2, 1.0])
    df.loc[df.index[2:6], 'bar'] = np.array([2.33j, 1.23 + 0.1j, 2.2, 1.0])
    result = df.loc[df.index[2:6], 'bar']
    expected = Series([2.33j, 1.23 + 0.1j, 2.2, 1.0], index=[3, 4, 5, 6], name='bar')
    tm.assert_series_equal(result, expected)
    df = DataFrame(index=Index(np.arange(1, 11)))
    df['foo'] = np.zeros(10, dtype=np.float64)
    df['bar'] = np.zeros(10, dtype=np.complex)
    with pytest.raises(ValueError):
        df[2:5] = np.arange(1, 4) * 1j