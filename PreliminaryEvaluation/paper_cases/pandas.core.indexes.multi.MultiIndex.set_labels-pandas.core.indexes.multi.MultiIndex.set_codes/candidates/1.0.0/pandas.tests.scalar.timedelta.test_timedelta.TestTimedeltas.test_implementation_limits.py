def test_implementation_limits(self):
    min_td = Timedelta(Timedelta.min)
    max_td = Timedelta(Timedelta.max)
    assert min_td.value == np.iinfo(np.int64).min + 1
    assert max_td.value == np.iinfo(np.int64).max
    assert min_td - Timedelta(1, 'ns') is NaT
    with pytest.raises(OverflowError):
        min_td - Timedelta(2, 'ns')
    with pytest.raises(OverflowError):
        max_td + Timedelta(1, 'ns')
    td = Timedelta(min_td.value - 1, 'ns')
    assert td is NaT
    with pytest.raises(OverflowError):
        Timedelta(min_td.value - 2, 'ns')
    with pytest.raises(OverflowError):
        Timedelta(max_td.value + 1, 'ns')