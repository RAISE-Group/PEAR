@pytest.mark.parametrize('index, dtype', [(pd.Int64Index, 'float64'), (pd.UInt64Index, 'categorical'), (pd.Float64Index, 'datetime64'), (pd.RangeIndex, 'float64')])
def test_invalid_dtype(self, index, dtype):
    with pytest.raises(ValueError, match=f'Incorrect `dtype` passed: expected \\w+(?: \\w+)?, received {dtype}'):
        index([1, 2, 3], dtype=dtype)