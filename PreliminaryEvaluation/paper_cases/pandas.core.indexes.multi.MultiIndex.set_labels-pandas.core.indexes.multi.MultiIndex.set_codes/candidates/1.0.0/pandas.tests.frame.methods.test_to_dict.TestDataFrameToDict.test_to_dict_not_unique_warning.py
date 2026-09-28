def test_to_dict_not_unique_warning(self):
    df = DataFrame([[1, 2, 3]], columns=['a', 'a', 'b'])
    with tm.assert_produces_warning(UserWarning):
        df.to_dict()