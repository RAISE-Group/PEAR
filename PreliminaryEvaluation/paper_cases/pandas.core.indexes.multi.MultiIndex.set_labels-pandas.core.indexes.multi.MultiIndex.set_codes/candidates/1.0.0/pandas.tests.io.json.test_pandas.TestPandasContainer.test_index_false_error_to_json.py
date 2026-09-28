@pytest.mark.parametrize('orient', ['records', 'index', 'columns', 'values'])
def test_index_false_error_to_json(self, orient):
    df = pd.DataFrame([[1, 2], [4, 5]], columns=['a', 'b'])
    msg = "'index=False' is only valid when 'orient' is 'split' or 'table'"
    with pytest.raises(ValueError, match=msg):
        df.to_json(orient=orient, index=False)