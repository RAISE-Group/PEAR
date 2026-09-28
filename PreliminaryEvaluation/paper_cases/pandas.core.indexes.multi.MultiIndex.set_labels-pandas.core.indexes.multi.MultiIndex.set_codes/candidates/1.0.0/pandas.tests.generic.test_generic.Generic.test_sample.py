def test_sample(self):
    o = self._construct(shape=10)
    for test in range(10):
        seed = np.random.randint(0, 100)
        self._compare(o.sample(n=4, random_state=seed), o.sample(n=4, random_state=seed))
        self._compare(o.sample(frac=0.7, random_state=seed), o.sample(frac=0.7, random_state=seed))
        self._compare(o.sample(n=4, random_state=np.random.RandomState(test)), o.sample(n=4, random_state=np.random.RandomState(test)))
        self._compare(o.sample(frac=0.7, random_state=np.random.RandomState(test)), o.sample(frac=0.7, random_state=np.random.RandomState(test)))
        self._compare(o.sample(frac=2, replace=True, random_state=np.random.RandomState(test)), o.sample(frac=2, replace=True, random_state=np.random.RandomState(test)))
        os1, os2 = ([], [])
        for _ in range(2):
            np.random.seed(test)
            os1.append(o.sample(n=4))
            os2.append(o.sample(frac=0.7))
        self._compare(*os1)
        self._compare(*os2)
    with pytest.raises(ValueError):
        o.sample(random_state='astring!')
    with pytest.raises(ValueError):
        o.sample(n=3, frac=0.3)
    with pytest.raises(ValueError):
        o.sample(n=-3)
    with pytest.raises(ValueError):
        o.sample(frac=-0.3)
    with pytest.raises(ValueError):
        o.sample(n=3.2)
    assert len(o.sample(n=4) == 4)
    assert len(o.sample(frac=0.34) == 3)
    assert len(o.sample(frac=0.36) == 4)
    with pytest.raises(ValueError):
        o.sample(n=3, weights=[0, 1])
    with pytest.raises(ValueError):
        bad_weights = [0.5] * 11
        o.sample(n=3, weights=bad_weights)
    with pytest.raises(ValueError):
        bad_weight_series = Series([0, 0, 0.2])
        o.sample(n=4, weights=bad_weight_series)
    with pytest.raises(ValueError):
        bad_weights = [-0.1] * 10
        o.sample(n=3, weights=bad_weights)
    with pytest.raises(ValueError):
        weights_with_inf = [0.1] * 10
        weights_with_inf[0] = np.inf
        o.sample(n=3, weights=weights_with_inf)
    with pytest.raises(ValueError):
        weights_with_ninf = [0.1] * 10
        weights_with_ninf[0] = -np.inf
        o.sample(n=3, weights=weights_with_ninf)
    zero_weights = [0] * 10
    with pytest.raises(ValueError):
        o.sample(n=3, weights=zero_weights)
    nan_weights = [np.nan] * 10
    with pytest.raises(ValueError):
        o.sample(n=3, weights=nan_weights)
    weights_with_nan = [np.nan] * 10
    weights_with_nan[5] = 0.5
    self._compare(o.sample(n=1, axis=0, weights=weights_with_nan), o.iloc[5:6])
    weights_with_None = [None] * 10
    weights_with_None[5] = 0.5
    self._compare(o.sample(n=1, axis=0, weights=weights_with_None), o.iloc[5:6])