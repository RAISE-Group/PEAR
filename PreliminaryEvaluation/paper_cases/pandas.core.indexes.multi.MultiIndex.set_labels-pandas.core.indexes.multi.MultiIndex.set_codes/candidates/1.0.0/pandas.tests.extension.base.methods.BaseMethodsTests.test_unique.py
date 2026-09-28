@pytest.mark.parametrize('box', [pd.Series, lambda x: x])
@pytest.mark.parametrize('method', [lambda x: x.unique(), pd.unique])
def test_unique(self, data, box, method):
    duplicated = box(data._from_sequence([data[0], data[0]]))
    result = method(duplicated)
    assert len(result) == 1
    assert isinstance(result, type(data))
    assert result[0] == duplicated[0]