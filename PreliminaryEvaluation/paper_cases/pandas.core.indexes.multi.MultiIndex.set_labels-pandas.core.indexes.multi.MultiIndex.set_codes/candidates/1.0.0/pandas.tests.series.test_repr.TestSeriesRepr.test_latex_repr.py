def test_latex_repr(self):
    result = '\\begin{tabular}{ll}\n\\toprule\n{} &         0 \\\\\n\\midrule\n0 &  $\\alpha$ \\\\\n1 &         b \\\\\n2 &         c \\\\\n\\bottomrule\n\\end{tabular}\n'
    with option_context('display.latex.escape', False, 'display.latex.repr', True):
        s = Series(['$\\alpha$', 'b', 'c'])
        assert result == s._repr_latex_()
    assert s._repr_latex_() is None