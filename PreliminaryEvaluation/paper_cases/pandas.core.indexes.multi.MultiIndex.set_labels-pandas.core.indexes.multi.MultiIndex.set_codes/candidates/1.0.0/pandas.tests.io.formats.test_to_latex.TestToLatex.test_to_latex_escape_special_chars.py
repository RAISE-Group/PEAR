def test_to_latex_escape_special_chars(self):
    special_characters = ['&', '%', '$', '#', '_', '{', '}', '~', '^', '\\']
    df = DataFrame(data=special_characters)
    observed = df.to_latex()
    expected = '\\begin{tabular}{ll}\n\\toprule\n{} &  0 \\\\\n\\midrule\n0 &  \\& \\\\\n1 &  \\% \\\\\n2 &  \\$ \\\\\n3 &  \\# \\\\\n4 &  \\_ \\\\\n5 &  \\{ \\\\\n6 &  \\} \\\\\n7 &  \\textasciitilde  \\\\\n8 &  \\textasciicircum  \\\\\n9 &  \\textbackslash  \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert observed == expected