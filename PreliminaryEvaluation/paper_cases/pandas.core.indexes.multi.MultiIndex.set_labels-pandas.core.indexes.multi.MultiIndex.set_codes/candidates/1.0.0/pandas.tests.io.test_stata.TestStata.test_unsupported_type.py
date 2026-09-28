def test_unsupported_type(self):
    original = pd.DataFrame({'a': [1 + 2j, 2 + 4j]})
    msg = 'Data type complex128 not supported'
    with pytest.raises(NotImplementedError, match=msg):
        with tm.ensure_clean() as path:
            original.to_stata(path)