def test_set_axis_name_raises(self):
    s = pd.Series([1])
    with pytest.raises(ValueError):
        s._set_axis_name(name='a', axis=1)