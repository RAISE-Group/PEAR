def test_applymap_subset_multiindex_code(self):
    codes = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])
    columns = pd.MultiIndex(levels=[['a', 'b'], ['%', '#']], codes=codes, names=['', ''])
    df = DataFrame([[1, -1, 1, 1], [-1, 1, 1, 1]], index=['hello', 'world'], columns=columns)
    pct_subset = pd.IndexSlice[:, pd.IndexSlice[:, '%':'%']]

    def color_negative_red(val):
        color = 'red' if val < 0 else 'black'
        return f'color: {color}'
    df.loc[pct_subset]
    df.style.applymap(color_negative_red, subset=pct_subset)