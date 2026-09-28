@pytest.mark.parametrize('version', [114, 117, 118, 119, None])
def test_encoding(self, version):
    raw = read_stata(self.dta_encoding)
    encoded = read_stata(self.dta_encoding)
    result = encoded.kreis1849[0]
    expected = raw.kreis1849[0]
    assert result == expected
    assert isinstance(result, str)
    with tm.ensure_clean() as path:
        encoded.to_stata(path, write_index=False, version=version)
        reread_encoded = read_stata(path)
        tm.assert_frame_equal(encoded, reread_encoded)