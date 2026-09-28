def test_invalid_dtype(self):
    msg = 'not understood'
    invalid_list = [pd.Timestamp, 'pd.Timestamp', list]
    for dtype in invalid_list:
        with pytest.raises(TypeError, match=msg):
            Series([], name='time', dtype=dtype)