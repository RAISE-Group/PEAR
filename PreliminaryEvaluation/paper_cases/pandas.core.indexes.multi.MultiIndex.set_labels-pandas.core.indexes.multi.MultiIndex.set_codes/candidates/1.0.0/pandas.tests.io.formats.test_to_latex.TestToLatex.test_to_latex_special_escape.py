def test_to_latex_special_escape(self):
    df = DataFrame(['a\\b\\c', '^a^b^c', '~a~b~c'])
    escaped_result = df.to_latex()
    escaped_expected = '\\begin{tabular}{ll}\n\\toprule\n{} &       0 \\\\\n\\midrule\n0 &   a\\textbackslash b\\textbackslash c \\\\\n1 &  \\textasciicircum a\\textasciicircum b\\textasciicircum c \\\\\n2 &  \\textasciitilde a\\textasciitilde b\\textasciitilde c \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert escaped_result == escaped_expected