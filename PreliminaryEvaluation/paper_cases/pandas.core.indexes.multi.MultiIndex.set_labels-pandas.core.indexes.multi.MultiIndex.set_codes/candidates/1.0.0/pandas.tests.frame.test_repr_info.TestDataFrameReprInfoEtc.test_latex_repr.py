def test_latex_repr(self):
    result = '\\begin{tabular}{llll}\n\\toprule\n{} &         0 &  1 &  2 \\\\\n\\midrule\n0 &  $\\alpha$ &  b &  c \\\\\n1 &         1 &  2 &  3 \\\\\n\\bottomrule\n\\end{tabular}\n'
    with option_context('display.latex.escape', False, 'display.latex.repr', True):
        df = DataFrame([['$\\alpha$', 'b', 'c'], [1, 2, 3]])
        assert result == df._repr_latex_()
    assert df._repr_latex_() is None