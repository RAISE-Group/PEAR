def check_result(self, result, expected):
    assert isinstance(result, FrozenList)
    assert result == expected