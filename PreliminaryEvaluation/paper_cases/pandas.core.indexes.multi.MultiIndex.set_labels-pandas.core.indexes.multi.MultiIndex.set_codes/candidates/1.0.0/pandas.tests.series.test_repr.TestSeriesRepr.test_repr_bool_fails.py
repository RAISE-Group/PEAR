def test_repr_bool_fails(self, capsys):
    s = Series([DataFrame(np.random.randn(2, 2)) for i in range(5)])
    repr(s)
    captured = capsys.readouterr()
    assert captured.err == ''