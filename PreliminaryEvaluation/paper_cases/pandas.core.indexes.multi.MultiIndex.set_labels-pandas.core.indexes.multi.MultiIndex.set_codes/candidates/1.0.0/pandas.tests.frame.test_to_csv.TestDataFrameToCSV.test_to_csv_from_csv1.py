def test_to_csv_from_csv1(self, float_frame, datetime_frame):
    with tm.ensure_clean('__tmp_to_csv_from_csv1__') as path:
        float_frame['A'][:5] = np.nan
        float_frame.to_csv(path)
        float_frame.to_csv(path, columns=['A', 'B'])
        float_frame.to_csv(path, header=False)
        float_frame.to_csv(path, index=False)
        datetime_frame.to_csv(path)
        recons = self.read_csv(path)
        tm.assert_frame_equal(datetime_frame, recons)
        datetime_frame.to_csv(path, index_label='index')
        recons = self.read_csv(path, index_col=None)
        assert len(recons.columns) == len(datetime_frame.columns) + 1
        datetime_frame.to_csv(path, index=False)
        recons = self.read_csv(path, index_col=None)
        tm.assert_almost_equal(datetime_frame.values, recons.values)
        dm = DataFrame({'s1': Series(range(3), index=np.arange(3)), 's2': Series(range(2), index=np.arange(2))})
        dm.to_csv(path)
        recons = self.read_csv(path)
        tm.assert_frame_equal(dm, recons)