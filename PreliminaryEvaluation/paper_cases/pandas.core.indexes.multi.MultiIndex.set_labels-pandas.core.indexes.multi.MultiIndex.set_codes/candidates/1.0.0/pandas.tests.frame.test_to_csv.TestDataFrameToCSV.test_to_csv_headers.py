def test_to_csv_headers(self):
    from_df = DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
    to_df = DataFrame([[1, 2], [3, 4]], columns=['X', 'Y'])
    with tm.ensure_clean('__tmp_to_csv_headers__') as path:
        from_df.to_csv(path, header=['X', 'Y'])
        recons = self.read_csv(path)
        tm.assert_frame_equal(to_df, recons)
        from_df.to_csv(path, index=False, header=['X', 'Y'])
        recons = self.read_csv(path)
        recons.reset_index(inplace=True)
        tm.assert_frame_equal(to_df, recons)