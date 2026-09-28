@pytest.mark.parametrize('df, to_replace, exp', [({'col1': [1, 2, 3], 'col2': [4, 5, 6]}, {4: 5, 5: 6, 6: 7}, {'col1': [1, 2, 3], 'col2': [5, 6, 7]}), ({'col1': [1, 2, 3], 'col2': ['4', '5', '6']}, {'4': '5', '5': '6', '6': '7'}, {'col1': [1, 2, 3], 'col2': ['5', '6', '7']})])
def test_replace_commutative(self, df, to_replace, exp):
    df = pd.DataFrame(df)
    expected = pd.DataFrame(exp)
    result = df.replace(to_replace)
    tm.assert_frame_equal(result, expected)