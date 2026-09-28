def test_td_add_sub_numeric_raises(self):
    td = Timedelta(10, unit='d')
    for other in [2, 2.0, np.int64(2), np.float64(2)]:
        with pytest.raises(TypeError):
            td + other
        with pytest.raises(TypeError):
            other + td
        with pytest.raises(TypeError):
            td - other
        with pytest.raises(TypeError):
            other - td