def test_add_series_with_extension_array(self, data):
    s = pd.Series(data)
    msg = "unsupported operand type\\(s\\) for \\+: \\'PeriodArray\\' and \\'PeriodArray\\'"
    with pytest.raises(TypeError, match=msg):
        s + data