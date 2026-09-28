def test_rolling_skew_eq_value_fperr(self):
    a = Series([1.1] * 15).rolling(window=10).skew()
    assert np.isnan(a).all()