@pytest.mark.parametrize('p_values, o_values, values, expected_values', [([Period('2019Q1', 'Q-DEC'), Period('2019Q2', 'Q-DEC')], [Period('2019Q1', 'Q-DEC'), Period('2019Q2', 'Q-DEC'), 'All'], [1.0, 1.0], [1.0, 1.0, np.nan]), ([Period('2019Q1', 'Q-DEC'), Period('2019Q2', 'Q-DEC')], [Period('2019Q1', 'Q-DEC'), Period('2019Q2', 'Q-DEC')], [1.0, 1.0], [1.0, 1.0])])
def test_period_reindex_with_object(self, p_values, o_values, values, expected_values):
    period_index = PeriodIndex(p_values)
    object_index = Index(o_values)
    s = pd.Series(values, index=period_index)
    result = s.reindex(object_index)
    expected = pd.Series(expected_values, index=object_index)
    tm.assert_series_equal(result, expected)