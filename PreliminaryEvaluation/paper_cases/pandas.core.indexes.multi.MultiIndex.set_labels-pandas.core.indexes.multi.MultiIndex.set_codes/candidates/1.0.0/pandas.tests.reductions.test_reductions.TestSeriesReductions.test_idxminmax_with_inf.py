def test_idxminmax_with_inf(self):
    s = pd.Series([0, -np.inf, np.inf, np.nan])
    assert s.idxmin() == 1
    assert np.isnan(s.idxmin(skipna=False))
    assert s.idxmax() == 2
    assert np.isnan(s.idxmax(skipna=False))
    with pd.option_context('mode.use_inf_as_na', True):
        assert s.idxmin() == 0
        assert np.isnan(s.idxmin(skipna=False))
        assert s.idxmax() == 0
        np.isnan(s.idxmax(skipna=False))