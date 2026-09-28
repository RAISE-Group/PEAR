@pytest.mark.parametrize('other', [pd.Timestamp.now(), pd.Timestamp.now().to_pydatetime(), pd.Timestamp.now().to_datetime64(), pd.date_range('2016-01-01', periods=3, freq='H'), pd.date_range('2016-01-01', periods=3, tz='Europe/Brussels'), pd.date_range('2016-01-01', periods=3, freq='S')._data, pd.date_range('2016-01-01', periods=3, tz='Asia/Tokyo')._data])
def test_parr_add_sub_invalid(self, other, box_with_array):
    rng = pd.period_range('1/1/2000', freq='D', periods=3)
    rng = tm.box_expected(rng, box_with_array)
    with pytest.raises(TypeError):
        rng + other
    with pytest.raises(TypeError):
        other + rng
    with pytest.raises(TypeError):
        rng - other
    with pytest.raises(TypeError):
        other - rng