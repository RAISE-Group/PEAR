def test_rdivmod_invalid(self):
    td = Timedelta(minutes=3)
    with pytest.raises(TypeError):
        divmod(Timestamp('2018-01-22'), td)
    with pytest.raises(TypeError):
        divmod(15, td)
    with pytest.raises(TypeError):
        divmod(16.0, td)
    with pytest.raises(TypeError):
        divmod(np.array([22, 24]), td)