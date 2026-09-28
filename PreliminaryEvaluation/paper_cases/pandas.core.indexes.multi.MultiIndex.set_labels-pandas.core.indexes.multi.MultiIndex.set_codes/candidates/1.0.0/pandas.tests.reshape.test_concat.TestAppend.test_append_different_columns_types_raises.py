@pytest.mark.parametrize('index_can_append', indexes_can_append, ids=lambda x: type(x).__name__)
@pytest.mark.parametrize('index_cannot_append_with_other', indexes_cannot_append_with_other, ids=lambda x: type(x).__name__)
def test_append_different_columns_types_raises(self, index_can_append, index_cannot_append_with_other):
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=index_can_append)
    ser = pd.Series([7, 8, 9], index=index_cannot_append_with_other, name=2)
    msg = "Expected tuple, got (int|long|float|str|pandas._libs.interval.Interval)|object of type '(int|float|Timestamp|pandas._libs.interval.Interval)' has no len\\(\\)|"
    with pytest.raises(TypeError, match=msg):
        df.append(ser)
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=index_cannot_append_with_other)
    ser = pd.Series([7, 8, 9], index=index_can_append, name=2)
    with pytest.raises(TypeError, match=msg):
        df.append(ser)