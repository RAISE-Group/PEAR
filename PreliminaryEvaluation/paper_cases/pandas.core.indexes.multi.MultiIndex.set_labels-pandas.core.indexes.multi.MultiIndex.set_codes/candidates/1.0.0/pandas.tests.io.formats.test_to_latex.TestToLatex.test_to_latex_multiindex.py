def test_to_latex_multiindex(self):
    df = DataFrame({('x', 'y'): ['a']})
    result = df.to_latex()
    expected = '\\begin{tabular}{ll}\n\\toprule\n{} &  x \\\\\n{} &  y \\\\\n\\midrule\n0 &  a \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert result == expected
    result = df.T.to_latex()
    expected = '\\begin{tabular}{lll}\n\\toprule\n  &   &  0 \\\\\n\\midrule\nx & y &  a \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert result == expected
    df = DataFrame.from_dict({('c1', 0): pd.Series({x: x for x in range(4)}), ('c1', 1): pd.Series({x: x + 4 for x in range(4)}), ('c2', 0): pd.Series({x: x for x in range(4)}), ('c2', 1): pd.Series({x: x + 4 for x in range(4)}), ('c3', 0): pd.Series({x: x for x in range(4)})}).T
    result = df.to_latex()
    expected = '\\begin{tabular}{llrrrr}\n\\toprule\n   &   &  0 &  1 &  2 &  3 \\\\\n\\midrule\nc1 & 0 &  0 &  1 &  2 &  3 \\\\\n   & 1 &  4 &  5 &  6 &  7 \\\\\nc2 & 0 &  0 &  1 &  2 &  3 \\\\\n   & 1 &  4 &  5 &  6 &  7 \\\\\nc3 & 0 &  0 &  1 &  2 &  3 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert result == expected
    df = df.T
    df.columns.names = ['a', 'b']
    result = df.to_latex()
    expected = '\\begin{tabular}{lrrrrr}\n\\toprule\na & \\multicolumn{2}{l}{c1} & \\multicolumn{2}{l}{c2} & c3 \\\\\nb &  0 &  1 &  0 &  1 &  0 \\\\\n\\midrule\n0 &  0 &  4 &  0 &  4 &  0 \\\\\n1 &  1 &  5 &  1 &  5 &  1 \\\\\n2 &  2 &  6 &  2 &  6 &  2 \\\\\n3 &  3 &  7 &  3 &  7 &  3 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert result == expected
    df = pd.DataFrame({'a': [0, 0, 1, 1], 'b': list('abab'), 'c': [1, 2, 3, 4]})
    result = df.set_index(['a', 'b']).to_latex()
    expected = '\\begin{tabular}{llr}\n\\toprule\n  &   &  c \\\\\na & b &    \\\\\n\\midrule\n0 & a &  1 \\\\\n  & b &  2 \\\\\n1 & a &  3 \\\\\n  & b &  4 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert result == expected
    result = df.groupby('a').describe().to_latex()
    expected = '\\begin{tabular}{lrrrrrrrr}\n\\toprule\n{} & \\multicolumn{8}{l}{c} \\\\\n{} & count & mean &       std &  min &   25\\% &  50\\% &   75\\% &  max \\\\\na &       &      &           &      &       &      &       &      \\\\\n\\midrule\n0 &   2.0 &  1.5 &  0.707107 &  1.0 &  1.25 &  1.5 &  1.75 &  2.0 \\\\\n1 &   2.0 &  3.5 &  0.707107 &  3.0 &  3.25 &  3.5 &  3.75 &  4.0 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert result == expected