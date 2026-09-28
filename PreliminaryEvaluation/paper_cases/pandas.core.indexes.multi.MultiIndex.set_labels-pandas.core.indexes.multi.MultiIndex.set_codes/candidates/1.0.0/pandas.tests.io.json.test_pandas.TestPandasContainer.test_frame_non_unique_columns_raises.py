@pytest.mark.parametrize('orient', ['index', 'columns', 'records'])
def test_frame_non_unique_columns_raises(self, orient):
    df = DataFrame([['a', 'b'], ['c', 'd']], index=[1, 2], columns=['x', 'x'])
    msg = f"DataFrame columns must be unique for orient='{orient}'"
    with pytest.raises(ValueError, match=msg):
        df.to_json(orient=orient)