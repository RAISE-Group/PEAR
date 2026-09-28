def test_sort_values_na_position_with_categories_raises(self):
    df = pd.DataFrame({'c': pd.Categorical(['A', np.nan, 'B', np.nan, 'C'], categories=['A', 'B', 'C'], ordered=True)})
    with pytest.raises(ValueError):
        df.sort_values(by='c', ascending=False, na_position='bad_position')