def test_rolling_min_max_numeric_types(self):
    types_test = [np.dtype('f{}'.format(width)) for width in [4, 8]]
    types_test.extend([np.dtype('{}{}'.format(sign, width)) for width in [1, 2, 4, 8] for sign in 'ui'])
    for data_type in types_test:
        result = DataFrame(np.arange(20, dtype=data_type)).rolling(window=5).max()
        assert result.dtypes[0] == np.dtype('f8')
        result = DataFrame(np.arange(20, dtype=data_type)).rolling(window=5).min()
        assert result.dtypes[0] == np.dtype('f8')