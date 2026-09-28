def test_to_latex_decimal(self, float_frame):
    float_frame.to_latex()
    df = DataFrame({'a': [1.0, 2.1], 'b': ['b1', 'b2']})
    withindex_result = df.to_latex(decimal=',')
    withindex_expected = '\\begin{tabular}{lrl}\n\\toprule\n{} &    a &   b \\\\\n\\midrule\n0 &  1,0 &  b1 \\\\\n1 &  2,1 &  b2 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert withindex_result == withindex_expected