def test_stack_order_with_unsorted_levels(self):

    def manual_compare_stacked(df, df_stacked, lev0, lev1):
        assert all((df.loc[row, col] == df_stacked.loc[(row, col[lev0]), col[lev1]] for row in df.index for col in df.columns))
    for width in [2, 3]:
        levels_poss = itertools.product(itertools.permutations([0, 1, 2], width), repeat=2)
        for levels in levels_poss:
            columns = MultiIndex(levels=levels, codes=[[0, 0, 1, 1], [0, 1, 0, 1]])
            df = DataFrame(columns=columns, data=[range(4)])
            for stack_lev in range(2):
                df_stacked = df.stack(stack_lev)
                manual_compare_stacked(df, df_stacked, stack_lev, 1 - stack_lev)
    mi = MultiIndex(levels=[['A', 'C', 'B'], ['B', 'A', 'C']], codes=[np.repeat(range(3), 3), np.tile(range(3), 3)])
    df = DataFrame(columns=mi, index=range(5), data=np.arange(5 * len(mi)).reshape(5, -1))
    manual_compare_stacked(df, df.stack(0), 0, 1)