def test_to_latex_format(self, float_frame):
    float_frame.to_latex(column_format='ccc')
    df = DataFrame({'a': [1, 2], 'b': ['b1', 'b2']})
    withindex_result = df.to_latex(column_format='ccc')
    withindex_expected = '\\begin{tabular}{ccc}\n\\toprule\n{} &  a &   b \\\\\n\\midrule\n0 &  1 &  b1 \\\\\n1 &  2 &  b2 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert withindex_result == withindex_expected