def test_groupby_extension_apply(self, data_for_grouping, groupby_apply_op):
    df = pd.DataFrame({'A': [1, 1, 2, 2, 3, 3, 1, 4], 'B': data_for_grouping})
    df.groupby('B').apply(groupby_apply_op)
    df.groupby('B').A.apply(groupby_apply_op)
    df.groupby('A').apply(groupby_apply_op)
    df.groupby('A').B.apply(groupby_apply_op)