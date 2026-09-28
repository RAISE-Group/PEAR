def test_to_latex_float_format_no_fixed_width(self):
    df = DataFrame({'x': [0.19999]})
    expected = '\\begin{tabular}{lr}\n\\toprule\n{} &     x \\\\\n\\midrule\n0 & 0.200 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert df.to_latex(float_format='%.3f') == expected
    df = DataFrame({'x': [100.0]})
    expected = '\\begin{tabular}{lr}\n\\toprule\n{} &   x \\\\\n\\midrule\n0 & 100 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert df.to_latex(float_format='%.0f') == expected