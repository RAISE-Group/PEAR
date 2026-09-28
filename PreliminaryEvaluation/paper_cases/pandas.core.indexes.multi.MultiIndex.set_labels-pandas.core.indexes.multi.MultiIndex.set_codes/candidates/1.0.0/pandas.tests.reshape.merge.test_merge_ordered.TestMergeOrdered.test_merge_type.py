def test_merge_type(self):

    class NotADataFrame(DataFrame):

        @property
        def _constructor(self):
            return NotADataFrame
    nad = NotADataFrame(self.left)
    result = nad.merge(self.right, on='key')
    assert isinstance(result, NotADataFrame)