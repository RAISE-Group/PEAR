@pytest.mark.parametrize('version', [114, 117, 118, 119, None])
def test_read_write_dta12(self, version):
    original = DataFrame([(1, 2, 3, 4, 5, 6)], columns=['astringwithmorethan32characters_1', 'astringwithmorethan32characters_2', '+', '-', 'short', 'delete'])
    formatted = DataFrame([(1, 2, 3, 4, 5, 6)], columns=['astringwithmorethan32characters_', '_0astringwithmorethan32character', '_', '_1_', '_short', '_delete'])
    formatted.index.name = 'index'
    formatted = formatted.astype(np.int32)
    with tm.ensure_clean() as path:
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always', InvalidColumnName)
            original.to_stata(path, None, version=version)
            assert len(w) == 1
        written_and_read_again = self.read_dta(path)
        tm.assert_frame_equal(written_and_read_again.set_index('index'), formatted)