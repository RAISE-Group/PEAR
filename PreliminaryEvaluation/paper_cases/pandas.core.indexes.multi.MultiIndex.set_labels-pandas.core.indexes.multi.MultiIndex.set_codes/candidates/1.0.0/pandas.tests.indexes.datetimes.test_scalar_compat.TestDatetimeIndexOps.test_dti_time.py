def test_dti_time(self):
    rng = date_range('1/1/2000', freq='12min', periods=10)
    result = pd.Index(rng).time
    expected = [t.time() for t in rng]
    assert (result == expected).all()