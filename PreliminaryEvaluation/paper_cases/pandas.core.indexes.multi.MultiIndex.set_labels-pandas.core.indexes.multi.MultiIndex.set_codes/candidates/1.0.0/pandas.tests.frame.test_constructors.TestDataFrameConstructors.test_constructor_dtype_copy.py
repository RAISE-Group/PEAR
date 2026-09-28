def test_constructor_dtype_copy(self):
    orig_df = DataFrame({'col1': [1.0], 'col2': [2.0], 'col3': [3.0]})
    new_df = pd.DataFrame(orig_df, dtype=float, copy=True)
    new_df['col1'] = 200.0
    assert orig_df['col1'][0] == 1.0