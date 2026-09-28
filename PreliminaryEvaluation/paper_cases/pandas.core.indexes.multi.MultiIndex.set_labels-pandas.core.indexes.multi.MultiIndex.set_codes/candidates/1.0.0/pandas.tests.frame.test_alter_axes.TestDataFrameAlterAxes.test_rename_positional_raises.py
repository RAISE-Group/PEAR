def test_rename_positional_raises(self):
    df = DataFrame(columns=['A', 'B'])
    msg = 'rename\\(\\) takes from 1 to 2 positional arguments'
    with pytest.raises(TypeError, match=msg):
        df.rename(None, str.lower)