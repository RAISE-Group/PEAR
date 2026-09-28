@pytest.mark.parametrize('method', ['min', 'max'])
def test_deprecate_numeric_only_min_max(self, method):
    cat = Categorical([np.nan, 1, 2, np.nan], categories=[5, 4, 3, 2, 1], ordered=True)
    with tm.assert_produces_warning(expected_warning=FutureWarning):
        getattr(cat, method)(numeric_only=True)