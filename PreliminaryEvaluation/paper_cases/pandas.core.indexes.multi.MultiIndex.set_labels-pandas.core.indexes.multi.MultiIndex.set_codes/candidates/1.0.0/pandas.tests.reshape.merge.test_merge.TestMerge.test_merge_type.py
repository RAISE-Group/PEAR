def test_merge_type(self):

    class NotADataFrame(DataFrame):

        @property
        def _constructor(self):
            return NotADataFrame
    nad = NotADataFrame(self.df)
    result = nad.merge(self.df2, on='key1')
    assert isinstance(result, NotADataFrame)