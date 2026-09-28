def test_dti_business_getitem(self):
    rng = pd.bdate_range(START, END)
    smaller = rng[:5]
    exp = DatetimeIndex(rng.view(np.ndarray)[:5])
    tm.assert_index_equal(smaller, exp)
    assert smaller.freq == rng.freq
    sliced = rng[::5]
    assert sliced.freq == BDay() * 5
    fancy_indexed = rng[[4, 3, 2, 1, 0]]
    assert len(fancy_indexed) == 5
    assert isinstance(fancy_indexed, DatetimeIndex)
    assert fancy_indexed.freq is None
    assert rng[4] == rng[np.int_(4)]