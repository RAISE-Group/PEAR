def test_negative_log(self):
    df = -DataFrame(rand(6, 4), index=list(string.ascii_letters[:6]), columns=['x', 'y', 'z', 'four'])
    with pytest.raises(ValueError):
        df.plot.area(logy=True)
    with pytest.raises(ValueError):
        df.plot.area(loglog=True)