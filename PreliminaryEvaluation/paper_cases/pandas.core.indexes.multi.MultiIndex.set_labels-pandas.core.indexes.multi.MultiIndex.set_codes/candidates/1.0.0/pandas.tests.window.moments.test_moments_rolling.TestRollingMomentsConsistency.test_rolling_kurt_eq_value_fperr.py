def test_rolling_kurt_eq_value_fperr(self):
    a = Series([1.1] * 15).rolling(window=10).kurt()
    assert np.isnan(a).all()