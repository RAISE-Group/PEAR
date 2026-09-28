def test_format_bug(self):
    now = datetime.now()
    if not str(now).endswith('000'):
        index = Index([now])
        formatted = index.format()
        expected = [str(index[0])]
        assert formatted == expected
    Index([]).format()