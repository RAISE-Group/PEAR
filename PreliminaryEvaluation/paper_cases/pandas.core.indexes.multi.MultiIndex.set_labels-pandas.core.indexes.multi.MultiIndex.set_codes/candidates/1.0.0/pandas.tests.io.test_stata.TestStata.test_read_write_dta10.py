@pytest.mark.parametrize('version', [114, 117, 118, 119, None])
def test_read_write_dta10(self, version):
    original = DataFrame(data=[['string', 'object', 1, 1.1, np.datetime64('2003-12-25')]], columns=['string', 'object', 'integer', 'floating', 'datetime'])
    original['object'] = Series(original['object'], dtype=object)
    original.index.name = 'index'
    original.index = original.index.astype(np.int32)
    original['integer'] = original['integer'].astype(np.int32)
    with tm.ensure_clean() as path:
        original.to_stata(path, {'datetime': 'tc'}, version=version)
        written_and_read_again = self.read_dta(path)
        tm.assert_frame_equal(written_and_read_again.set_index('index'), original, check_index_type=False)