def test_from_records_columns_not_modified(self):
    tuples = [(1, 2, 3), (1, 2, 3), (2, 5, 3)]
    columns = ['a', 'b', 'c']
    original_columns = list(columns)
    df = DataFrame.from_records(tuples, columns=columns, index='a')
    assert columns == original_columns