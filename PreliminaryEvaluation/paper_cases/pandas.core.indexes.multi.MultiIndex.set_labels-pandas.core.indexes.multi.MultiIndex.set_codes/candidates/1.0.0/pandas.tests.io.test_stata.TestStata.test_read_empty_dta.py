@pytest.mark.parametrize('version', [114, 117, 118, 119, None])
def test_read_empty_dta(self, version):
    empty_ds = DataFrame(columns=['unit'])
    with tm.ensure_clean() as path:
        empty_ds.to_stata(path, write_index=False, version=version)
        empty_ds2 = read_stata(path)
        tm.assert_frame_equal(empty_ds, empty_ds2)