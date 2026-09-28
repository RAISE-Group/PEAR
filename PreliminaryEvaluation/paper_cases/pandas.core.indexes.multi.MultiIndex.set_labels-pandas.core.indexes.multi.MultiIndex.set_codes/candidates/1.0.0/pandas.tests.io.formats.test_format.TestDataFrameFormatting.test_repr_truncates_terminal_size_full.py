def test_repr_truncates_terminal_size_full(self, monkeypatch):
    terminal_size = (80, 24)
    df = pd.DataFrame(np.random.rand(1, 7))
    monkeypatch.setattr('pandas.io.formats.format.get_terminal_size', lambda: terminal_size)
    assert '...' not in str(df)