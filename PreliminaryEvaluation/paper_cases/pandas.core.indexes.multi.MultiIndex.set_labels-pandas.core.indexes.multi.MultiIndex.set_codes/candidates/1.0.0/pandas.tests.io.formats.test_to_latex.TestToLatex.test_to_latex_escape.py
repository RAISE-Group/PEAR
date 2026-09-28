def test_to_latex_escape(self):
    a = 'a'
    b = 'b'
    test_dict = {'co$e^x$': {a: 'a', b: 'b'}, 'co^l1': {a: 'a', b: 'b'}}
    unescaped_result = DataFrame(test_dict).to_latex(escape=False)
    escaped_result = DataFrame(test_dict).to_latex()
    unescaped_expected = '\\begin{tabular}{lll}\n\\toprule\n{} & co$e^x$ & co^l1 \\\\\n\\midrule\na &       a &     a \\\\\nb &       b &     b \\\\\n\\bottomrule\n\\end{tabular}\n'
    escaped_expected = '\\begin{tabular}{lll}\n\\toprule\n{} & co\\$e\\textasciicircum x\\$ & co\\textasciicircum l1 \\\\\n\\midrule\na &       a &     a \\\\\nb &       b &     b \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert unescaped_result == unescaped_expected
    assert escaped_result == escaped_expected