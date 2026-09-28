def test_to_latex_multicolumnrow(self):
    df = pd.DataFrame({('c1', 0): {x: x for x in range(5)}, ('c1', 1): {x: x + 5 for x in range(5)}, ('c2', 0): {x: x for x in range(5)}, ('c2', 1): {x: x + 5 for x in range(5)}, ('c3', 0): {x: x for x in range(5)}})
    result = df.to_latex()
    expected = '\\begin{tabular}{lrrrrr}\n\\toprule\n{} & \\multicolumn{2}{l}{c1} & \\multicolumn{2}{l}{c2} & c3 \\\\\n{} &  0 &  1 &  0 &  1 &  0 \\\\\n\\midrule\n0 &  0 &  5 &  0 &  5 &  0 \\\\\n1 &  1 &  6 &  1 &  6 &  1 \\\\\n2 &  2 &  7 &  2 &  7 &  2 \\\\\n3 &  3 &  8 &  3 &  8 &  3 \\\\\n4 &  4 &  9 &  4 &  9 &  4 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert result == expected
    result = df.to_latex(multicolumn=False)
    expected = '\\begin{tabular}{lrrrrr}\n\\toprule\n{} & c1 &    & c2 &    & c3 \\\\\n{} &  0 &  1 &  0 &  1 &  0 \\\\\n\\midrule\n0 &  0 &  5 &  0 &  5 &  0 \\\\\n1 &  1 &  6 &  1 &  6 &  1 \\\\\n2 &  2 &  7 &  2 &  7 &  2 \\\\\n3 &  3 &  8 &  3 &  8 &  3 \\\\\n4 &  4 &  9 &  4 &  9 &  4 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert result == expected
    result = df.T.to_latex(multirow=True)
    expected = '\\begin{tabular}{llrrrrr}\n\\toprule\n   &   &  0 &  1 &  2 &  3 &  4 \\\\\n\\midrule\n\\multirow{2}{*}{c1} & 0 &  0 &  1 &  2 &  3 &  4 \\\\\n   & 1 &  5 &  6 &  7 &  8 &  9 \\\\\n\\cline{1-7}\n\\multirow{2}{*}{c2} & 0 &  0 &  1 &  2 &  3 &  4 \\\\\n   & 1 &  5 &  6 &  7 &  8 &  9 \\\\\n\\cline{1-7}\nc3 & 0 &  0 &  1 &  2 &  3 &  4 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert result == expected
    df.index = df.T.index
    result = df.T.to_latex(multirow=True, multicolumn=True, multicolumn_format='c')
    expected = '\\begin{tabular}{llrrrrr}\n\\toprule\n   &   & \\multicolumn{2}{c}{c1} & \\multicolumn{2}{c}{c2} & c3 \\\\\n   &   &  0 &  1 &  0 &  1 &  0 \\\\\n\\midrule\n\\multirow{2}{*}{c1} & 0 &  0 &  1 &  2 &  3 &  4 \\\\\n   & 1 &  5 &  6 &  7 &  8 &  9 \\\\\n\\cline{1-7}\n\\multirow{2}{*}{c2} & 0 &  0 &  1 &  2 &  3 &  4 \\\\\n   & 1 &  5 &  6 &  7 &  8 &  9 \\\\\n\\cline{1-7}\nc3 & 0 &  0 &  1 &  2 &  3 &  4 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert result == expected