@pytest.mark.parametrize('version', [114, 117, 118, 119, None])
def test_invalid_file_not_written(self, version):
    content = 'Here is one __�__ Another one __·__ Another one __½__'
    df = DataFrame([content], columns=['invalid'])
    with tm.ensure_clean() as path:
        msg1 = "'latin-1' codec can't encode character '\\\\ufffd' in position 14: ordinal not in range\\(256\\)"
        msg2 = "'ascii' codec can't decode byte 0xef in position 14: ordinal not in range\\(128\\)"
        with pytest.raises(UnicodeEncodeError, match='{}|{}'.format(msg1, msg2)):
            with tm.assert_produces_warning(ResourceWarning):
                df.to_stata(path)