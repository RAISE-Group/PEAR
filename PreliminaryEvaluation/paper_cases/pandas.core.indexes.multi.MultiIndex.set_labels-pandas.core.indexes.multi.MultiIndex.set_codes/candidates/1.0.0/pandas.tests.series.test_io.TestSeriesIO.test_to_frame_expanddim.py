def test_to_frame_expanddim(self):

    class SubclassedSeries(Series):

        @property
        def _constructor_expanddim(self):
            return SubclassedFrame

    class SubclassedFrame(DataFrame):
        pass
    s = SubclassedSeries([1, 2, 3], name='X')
    result = s.to_frame()
    assert isinstance(result, SubclassedFrame)
    expected = SubclassedFrame({'X': [1, 2, 3]})
    tm.assert_frame_equal(result, expected)