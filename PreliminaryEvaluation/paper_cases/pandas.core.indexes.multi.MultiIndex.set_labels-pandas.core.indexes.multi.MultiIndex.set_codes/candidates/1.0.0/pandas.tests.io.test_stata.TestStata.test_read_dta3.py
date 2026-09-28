@pytest.mark.parametrize('file', ['dta3_113', 'dta3_114', 'dta3_115', 'dta3_117'])
def test_read_dta3(self, file):
    file = getattr(self, file)
    parsed = self.read_dta(file)
    expected = self.read_csv(self.csv3)
    expected = expected.astype(np.float32)
    expected['year'] = expected['year'].astype(np.int16)
    expected['quarter'] = expected['quarter'].astype(np.int8)
    tm.assert_frame_equal(parsed, expected)