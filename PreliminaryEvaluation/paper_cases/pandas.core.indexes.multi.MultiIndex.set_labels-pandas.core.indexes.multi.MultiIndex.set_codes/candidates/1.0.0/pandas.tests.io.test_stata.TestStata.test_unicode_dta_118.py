def test_unicode_dta_118(self):
    unicode_df = self.read_dta(self.dta25_118)
    columns = ['utf8', 'latin1', 'ascii', 'utf8_strl', 'ascii_strl']
    values = [['ραηδας', 'PÄNDÄS', 'p', 'ραηδας', 'p'], ['ƤĀńĐąŜ', 'Ö', 'a', 'ƤĀńĐąŜ', 'a'], ['ᴘᴀᴎᴅᴀS', 'Ü', 'n', 'ᴘᴀᴎᴅᴀS', 'n'], ['      ', '      ', 'd', '      ', 'd'], [' ', '', 'a', ' ', 'a'], ['', '', 's', '', 's'], ['', '', ' ', '', ' ']]
    expected = pd.DataFrame(values, columns=columns)
    tm.assert_frame_equal(unicode_df, expected)