@pytest.mark.parametrize('box', [pd.Timestamp, 'pd.Timestamp', list])
def test_invalid_dtype_error(self, box):
    with pytest.raises(TypeError, match='not understood'):
        com.pandas_dtype(box)