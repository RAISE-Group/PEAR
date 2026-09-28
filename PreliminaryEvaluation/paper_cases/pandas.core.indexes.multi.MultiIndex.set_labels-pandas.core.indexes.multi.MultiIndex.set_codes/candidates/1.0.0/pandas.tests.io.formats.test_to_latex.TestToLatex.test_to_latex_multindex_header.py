def test_to_latex_multindex_header(self):
    df = pd.DataFrame({'a': [0], 'b': [1], 'c': [2], 'd': [3]}).set_index(['a', 'b'])
    observed = df.to_latex(header=['r1', 'r2'])
    expected = '\\begin{tabular}{llrr}\n\\toprule\n  &   & r1 & r2 \\\\\na & b &    &    \\\\\n\\midrule\n0 & 1 &  2 &  3 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert observed == expected