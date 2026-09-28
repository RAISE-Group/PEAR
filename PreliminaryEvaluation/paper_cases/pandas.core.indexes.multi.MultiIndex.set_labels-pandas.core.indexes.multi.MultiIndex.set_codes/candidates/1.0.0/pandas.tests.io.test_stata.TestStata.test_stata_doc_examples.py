def test_stata_doc_examples(self):
    with tm.ensure_clean() as path:
        df = DataFrame(np.random.randn(10, 2), columns=list('AB'))
        df.to_stata(path)