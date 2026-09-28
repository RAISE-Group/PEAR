def test_rmod_invalid(self):
    td = Timedelta(minutes=3)
    with pytest.raises(TypeError):
        Timestamp('2018-01-22') % td
    with pytest.raises(TypeError):
        15 % td
    with pytest.raises(TypeError):
        16.0 % td
    with pytest.raises(TypeError):
        np.array([22, 24]) % td