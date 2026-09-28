def test_merge_two_empty_df_no_division_error(self):
    a = pd.DataFrame({'a': [], 'b': [], 'c': []})
    with np.errstate(divide='raise'):
        merge(a, a, on=('a', 'b'))