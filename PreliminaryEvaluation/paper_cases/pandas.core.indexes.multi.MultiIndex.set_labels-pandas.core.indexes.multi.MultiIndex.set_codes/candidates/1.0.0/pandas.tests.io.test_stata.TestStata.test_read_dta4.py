@pytest.mark.parametrize('file', ['dta4_113', 'dta4_114', 'dta4_115', 'dta4_117'])
def test_read_dta4(self, file):
    file = getattr(self, file)
    parsed = self.read_dta(file)
    expected = DataFrame.from_records([['one', 'ten', 'one', 'one', 'one'], ['two', 'nine', 'two', 'two', 'two'], ['three', 'eight', 'three', 'three', 'three'], ['four', 'seven', 4, 'four', 'four'], ['five', 'six', 5, np.nan, 'five'], ['six', 'five', 6, np.nan, 'six'], ['seven', 'four', 7, np.nan, 'seven'], ['eight', 'three', 8, np.nan, 'eight'], ['nine', 'two', 9, np.nan, 'nine'], ['ten', 'one', 'ten', np.nan, 'ten']], columns=['fully_labeled', 'fully_labeled2', 'incompletely_labeled', 'labeled_with_missings', 'float_labelled'])
    expected = pd.concat([expected[col].astype('category') for col in expected], axis=1)
    tm.assert_frame_equal(parsed, expected, check_categorical=False)