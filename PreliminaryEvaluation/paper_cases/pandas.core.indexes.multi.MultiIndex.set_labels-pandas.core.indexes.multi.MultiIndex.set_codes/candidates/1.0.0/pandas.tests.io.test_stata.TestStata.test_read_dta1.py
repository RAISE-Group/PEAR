@pytest.mark.parametrize('file', ['dta1_114', 'dta1_117'])
def test_read_dta1(self, file):
    file = getattr(self, file)
    parsed = self.read_dta(file)
    expected = DataFrame([(np.nan, np.nan, np.nan, np.nan, np.nan)], columns=['float_miss', 'double_miss', 'byte_miss', 'int_miss', 'long_miss'])
    expected['float_miss'] = expected['float_miss'].astype(np.float32)
    tm.assert_frame_equal(parsed, expected)