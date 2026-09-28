def test_encoding_latin1_118(self):
    msg = '\nOne or more strings in the dta file could not be decoded using utf-8, and\nso the fallback encoding of latin-1 is being used.  This can happen when a file\nhas been incorrectly encoded by Stata or some other software. You should verify\nthe string values returned are correct.'
    with tm.assert_produces_warning(UnicodeWarning) as w:
        encoded = read_stata(self.dta_encoding_118)
        assert len(w) == 151
        assert w[0].message.args[0] == msg
    expected = pd.DataFrame([['Düsseldorf']] * 151, columns=['kreis1849'])
    tm.assert_frame_equal(encoded, expected)