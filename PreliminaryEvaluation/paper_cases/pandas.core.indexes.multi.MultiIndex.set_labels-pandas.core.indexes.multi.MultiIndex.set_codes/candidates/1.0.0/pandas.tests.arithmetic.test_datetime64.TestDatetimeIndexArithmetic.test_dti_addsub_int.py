def test_dti_addsub_int(self, tz_naive_fixture, one):
    tz = tz_naive_fixture
    rng = pd.date_range('2000-01-01 09:00', freq='H', periods=10, tz=tz)
    msg = 'Addition/subtraction of integers'
    with pytest.raises(TypeError, match=msg):
        rng + one
    with pytest.raises(TypeError, match=msg):
        rng += one
    with pytest.raises(TypeError, match=msg):
        rng - one
    with pytest.raises(TypeError, match=msg):
        rng -= one