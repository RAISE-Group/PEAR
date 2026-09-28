def test_to_csv_multiindex(self, float_frame, datetime_frame):
    frame = float_frame
    old_index = frame.index
    arrays = np.arange(len(old_index) * 2).reshape(2, -1)
    new_index = MultiIndex.from_arrays(arrays, names=['first', 'second'])
    frame.index = new_index
    with tm.ensure_clean('__tmp_to_csv_multiindex__') as path:
        frame.to_csv(path, header=False)
        frame.to_csv(path, columns=['A', 'B'])
        frame.to_csv(path)
        df = self.read_csv(path, index_col=[0, 1], parse_dates=False)
        tm.assert_frame_equal(frame, df, check_names=False)
        assert frame.index.names == df.index.names
        float_frame.index = old_index
        tsframe = datetime_frame
        old_index = tsframe.index
        new_index = [old_index, np.arange(len(old_index))]
        tsframe.index = MultiIndex.from_arrays(new_index)
        tsframe.to_csv(path, index_label=['time', 'foo'])
        recons = self.read_csv(path, index_col=[0, 1])
        tm.assert_frame_equal(tsframe, recons, check_names=False)
        tsframe.to_csv(path)
        recons = self.read_csv(path, index_col=None)
        assert len(recons.columns) == len(tsframe.columns) + 2
        tsframe.to_csv(path, index=False)
        recons = self.read_csv(path, index_col=None)
        tm.assert_almost_equal(recons.values, datetime_frame.values)
        datetime_frame.index = old_index
    with tm.ensure_clean('__tmp_to_csv_multiindex__') as path:

        def _make_frame(names=None):
            if names is True:
                names = ['first', 'second']
            return DataFrame(np.random.randint(0, 10, size=(3, 3)), columns=MultiIndex.from_tuples([('bah', 'foo'), ('bah', 'bar'), ('ban', 'baz')], names=names), dtype='int64')
        df = tm.makeCustomDataframe(5, 3, r_idx_nlevels=2, c_idx_nlevels=4)
        df.to_csv(path)
        result = read_csv(path, header=[0, 1, 2, 3], index_col=[0, 1])
        tm.assert_frame_equal(df, result)
        df = tm.makeCustomDataframe(5, 3, r_idx_nlevels=1, c_idx_nlevels=4)
        df.to_csv(path)
        result = read_csv(path, header=[0, 1, 2, 3], index_col=0)
        tm.assert_frame_equal(df, result)
        df = tm.makeCustomDataframe(5, 3, r_idx_nlevels=3, c_idx_nlevels=4)
        df.to_csv(path)
        result = read_csv(path, header=[0, 1, 2, 3], index_col=[0, 1, 2])
        tm.assert_frame_equal(df, result)
        df = _make_frame()
        df.to_csv(path, index=False)
        result = read_csv(path, header=[0, 1])
        tm.assert_frame_equal(df, result)
        df = _make_frame(True)
        df.to_csv(path, index=False)
        result = read_csv(path, header=[0, 1])
        assert com.all_none(*result.columns.names)
        result.columns.names = df.columns.names
        tm.assert_frame_equal(df, result)
        df = _make_frame()
        df.to_csv(path)
        result = read_csv(path, header=[0, 1], index_col=[0])
        tm.assert_frame_equal(df, result)
        df = _make_frame(True)
        df.to_csv(path)
        result = read_csv(path, header=[0, 1], index_col=[0])
        tm.assert_frame_equal(df, result)
        df = _make_frame(True)
        df.to_csv(path)
        for i in [6, 7]:
            msg = 'len of {i}, but only 5 lines in file'.format(i=i)
            with pytest.raises(ParserError, match=msg):
                read_csv(path, header=list(range(i)), index_col=0)
        msg = 'cannot specify cols with a MultiIndex'
        with pytest.raises(TypeError, match=msg):
            df.to_csv(path, columns=['foo', 'bar'])
    with tm.ensure_clean('__tmp_to_csv_multiindex__') as path:
        tsframe[:0].to_csv(path)
        recons = self.read_csv(path)
        exp = tsframe[:0]
        exp.index = []
        tm.assert_index_equal(recons.columns, exp.columns)
        assert len(recons) == 0