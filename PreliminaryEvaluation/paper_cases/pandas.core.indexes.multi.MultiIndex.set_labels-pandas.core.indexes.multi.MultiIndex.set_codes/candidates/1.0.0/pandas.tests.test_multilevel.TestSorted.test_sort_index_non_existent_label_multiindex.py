def test_sort_index_non_existent_label_multiindex(self):
    df = DataFrame(0, columns=[], index=pd.MultiIndex.from_product([[], []]))
    df.loc['b', '2'] = 1
    df.loc['a', '3'] = 1
    result = df.sort_index().index.is_monotonic
    assert result is True