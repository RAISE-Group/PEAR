def test_append_join_nondatetimeindex(self):
    rng = date_range('1/1/2000', periods=10)
    idx = Index(['a', 'b', 'c', 'd'])
    result = rng.append(idx)
    assert isinstance(result[0], Timestamp)
    rng.join(idx, how='outer')