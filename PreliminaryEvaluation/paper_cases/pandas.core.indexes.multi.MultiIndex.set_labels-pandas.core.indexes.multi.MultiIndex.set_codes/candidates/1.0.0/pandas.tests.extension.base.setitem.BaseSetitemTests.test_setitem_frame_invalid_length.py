def test_setitem_frame_invalid_length(self, data):
    df = pd.DataFrame({'A': [1] * len(data)})
    xpr = 'Length of values does not match length of index'
    with pytest.raises(ValueError, match=xpr):
        df['B'] = data[:5]