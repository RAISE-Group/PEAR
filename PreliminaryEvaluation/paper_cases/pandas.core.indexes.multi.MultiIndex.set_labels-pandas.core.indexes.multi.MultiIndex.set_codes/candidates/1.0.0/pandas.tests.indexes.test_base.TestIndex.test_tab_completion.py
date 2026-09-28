@pytest.mark.parametrize('index,expected', [(Index(list('abcd')), True), (Index(range(4)), False)])
def test_tab_completion(self, index, expected):
    result = 'str' in dir(index)
    assert result == expected