def test_getitem_single_list_of_columns(self, df):
    with tm.assert_produces_warning(FutureWarning):
        df.groupby('A')['C', 'D'].mean()