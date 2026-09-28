def test_path(self):
    with tm.ensure_clean('test.json') as path:
        for df in [self.frame, self.frame2, self.intframe, self.tsframe, self.mixed_frame]:
            df.to_json(path)
            read_json(path)