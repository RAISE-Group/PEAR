def test_float_index_at_iat(self):
    s = Series([1, 2, 3], index=[0.1, 0.2, 0.3])
    for el, item in s.items():
        assert s.at[el] == item
    for i in range(len(s)):
        assert s.iat[i] == i + 1