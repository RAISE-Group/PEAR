def test_to_latex_multiindex_empty_name(self):
    mi = pd.MultiIndex.from_product([[1, 2]], names=[''])
    df = pd.DataFrame(-1, index=mi, columns=range(4))
    observed = df.to_latex()
    expected = '\\begin{tabular}{lrrrr}\n\\toprule\n  &  0 &  1 &  2 &  3 \\\\\n{} &    &    &    &    \\\\\n\\midrule\n1 & -1 & -1 & -1 & -1 \\\\\n2 & -1 & -1 & -1 & -1 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert observed == expected