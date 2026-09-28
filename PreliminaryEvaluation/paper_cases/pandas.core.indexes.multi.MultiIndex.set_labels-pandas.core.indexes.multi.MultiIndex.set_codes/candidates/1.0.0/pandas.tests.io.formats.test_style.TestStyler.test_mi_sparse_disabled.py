def test_mi_sparse_disabled(self):
    with pd.option_context('display.multi_sparse', False):
        df = pd.DataFrame({'A': [1, 2]}, index=pd.MultiIndex.from_arrays([['a', 'a'], [0, 1]]))
        result = df.style._translate()
    body = result['body']
    for row in body:
        assert 'attributes' not in row[0]