def test_pi_add_sub_td64_array_non_tick_raises(self):
    rng = pd.period_range('1/1/2000', freq='Q', periods=3)
    tdi = pd.TimedeltaIndex(['-1 Day', '-1 Day', '-1 Day'])
    tdarr = tdi.values
    with pytest.raises(IncompatibleFrequency):
        rng + tdarr
    with pytest.raises(IncompatibleFrequency):
        tdarr + rng
    with pytest.raises(IncompatibleFrequency):
        rng - tdarr
    with pytest.raises(TypeError):
        tdarr - rng