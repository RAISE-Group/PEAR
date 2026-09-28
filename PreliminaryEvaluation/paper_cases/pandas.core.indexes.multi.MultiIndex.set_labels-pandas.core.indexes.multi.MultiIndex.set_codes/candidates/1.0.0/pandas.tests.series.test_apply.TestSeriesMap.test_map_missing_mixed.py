@pytest.mark.parametrize('vals,mapping,exp', [(list('abc'), {np.nan: 'not NaN'}, [np.nan] * 3 + ['not NaN']), (list('abc'), {'a': 'a letter'}, ['a letter'] + [np.nan] * 3), (list(range(3)), {0: 42}, [42] + [np.nan] * 3)])
def test_map_missing_mixed(self, vals, mapping, exp):
    s = pd.Series(vals + [np.nan])
    result = s.map(mapping)
    tm.assert_series_equal(result, pd.Series(exp))