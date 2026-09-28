def test_add_series_with_extension_array(self, data):
    s = pd.Series(data)
    msg = 'cannot add DatetimeArray and DatetimeArray'
    with pytest.raises(TypeError, match=msg):
        s + data