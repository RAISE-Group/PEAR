@pytest.mark.parametrize('emptylike,expected_index,expected_columns', [([[]], RangeIndex(1), RangeIndex(0)), ([[], []], RangeIndex(2), RangeIndex(0)), ([(_ for _ in [])], RangeIndex(1), RangeIndex(0))])
def test_emptylike_constructor(self, emptylike, expected_index, expected_columns):
    expected = DataFrame(index=expected_index, columns=expected_columns)
    result = DataFrame(emptylike)
    tm.assert_frame_equal(result, expected)