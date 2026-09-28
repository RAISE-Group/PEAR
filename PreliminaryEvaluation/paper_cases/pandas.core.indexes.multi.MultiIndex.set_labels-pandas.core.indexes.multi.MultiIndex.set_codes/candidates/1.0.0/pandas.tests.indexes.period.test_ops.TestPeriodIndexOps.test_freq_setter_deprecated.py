def test_freq_setter_deprecated(self):
    idx = pd.period_range('2018Q1', periods=4, freq='Q')
    with tm.assert_produces_warning(None):
        idx.freq
    with pytest.raises(AttributeError, match="can't set attribute"):
        idx.freq = pd.offsets.Day()