@pytest.mark.parametrize('compression', ['', 'None', 'bad', '7z'])
def test_write_explicit_bad(self, compression, get_random_path):
    with pytest.raises(ValueError, match='Unrecognized compression type'):
        with tm.ensure_clean(get_random_path) as path:
            df = tm.makeDataFrame()
            df.to_pickle(path, compression=compression)