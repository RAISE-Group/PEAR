def test_to_latex_filename(self, float_frame):
    with tm.ensure_clean('test.tex') as path:
        float_frame.to_latex(path)
        with open(path, 'r') as f:
            assert float_frame.to_latex() == f.read()
    df = DataFrame([['außgangen']])
    with tm.ensure_clean('test.tex') as path:
        df.to_latex(path, encoding='utf-8')
        with codecs.open(path, 'r', encoding='utf-8') as f:
            assert df.to_latex() == f.read()
    with tm.ensure_clean('test.tex') as path:
        df.to_latex(path)
        with codecs.open(path, 'r', encoding='utf-8') as f:
            assert df.to_latex() == f.read()