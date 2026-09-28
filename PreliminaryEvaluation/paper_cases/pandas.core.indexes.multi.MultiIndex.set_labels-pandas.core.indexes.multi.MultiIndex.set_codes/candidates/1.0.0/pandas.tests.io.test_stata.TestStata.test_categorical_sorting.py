@pytest.mark.parametrize('file', ['dta20_115', 'dta20_117'])
def test_categorical_sorting(self, file):
    parsed = read_stata(getattr(self, file))
    parsed = parsed.sort_values('srh', na_position='first')
    parsed.index = np.arange(parsed.shape[0])
    codes = [-1, -1, 0, 1, 1, 1, 2, 2, 3, 4]
    categories = ['Poor', 'Fair', 'Good', 'Very good', 'Excellent']
    cat = pd.Categorical.from_codes(codes=codes, categories=categories)
    expected = pd.Series(cat, name='srh')
    tm.assert_series_equal(expected, parsed['srh'], check_categorical=False)