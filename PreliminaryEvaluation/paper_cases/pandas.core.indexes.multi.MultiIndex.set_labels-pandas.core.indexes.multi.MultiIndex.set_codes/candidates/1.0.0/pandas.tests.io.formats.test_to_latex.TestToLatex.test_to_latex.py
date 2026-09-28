def test_to_latex(self, float_frame):
    float_frame.to_latex()
    df = DataFrame({'a': [1, 2], 'b': ['b1', 'b2']})
    withindex_result = df.to_latex()
    withindex_expected = '\\begin{tabular}{lrl}\n\\toprule\n{} &  a &   b \\\\\n\\midrule\n0 &  1 &  b1 \\\\\n1 &  2 &  b2 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert withindex_result == withindex_expected
    withoutindex_result = df.to_latex(index=False)
    withoutindex_expected = '\\begin{tabular}{rl}\n\\toprule\n a &   b \\\\\n\\midrule\n 1 &  b1 \\\\\n 2 &  b2 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert withoutindex_result == withoutindex_expected