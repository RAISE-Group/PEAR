def test_mi_intervalindex_slicing_with_scalar(self):
    idx = pd.MultiIndex.from_arrays([pd.Index(['FC', 'FC', 'FC', 'FC', 'OWNER', 'OWNER', 'OWNER', 'OWNER']), pd.Index(['RID1', 'RID1', 'RID2', 'RID2', 'RID1', 'RID1', 'RID2', 'RID2']), pd.IntervalIndex.from_arrays([0, 1, 10, 11, 0, 1, 10, 11], [1, 2, 11, 12, 1, 2, 11, 12])])
    idx.names = ['Item', 'RID', 'MP']
    df = pd.DataFrame({'value': [1, 2, 3, 4, 5, 6, 7, 8]})
    df.index = idx
    query_df = pd.DataFrame({'Item': ['FC', 'OWNER', 'FC', 'OWNER', 'OWNER'], 'RID': ['RID1', 'RID1', 'RID1', 'RID2', 'RID2'], 'MP': [0.2, 1.5, 1.6, 11.1, 10.9]})
    query_df = query_df.sort_index()
    idx = pd.MultiIndex.from_arrays([query_df.Item, query_df.RID, query_df.MP])
    query_df.index = idx
    result = df.value.loc[query_df.index]
    expected = pd.Series([1, 6, 2, 8, 7], index=idx, name='value')
    tm.assert_series_equal(result, expected)