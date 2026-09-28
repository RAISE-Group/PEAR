def test_take_pandas_style_negative_raises(self, data, na_value):
    with pytest.raises(ValueError):
        data.take([0, -2], fill_value=na_value, allow_fill=True)