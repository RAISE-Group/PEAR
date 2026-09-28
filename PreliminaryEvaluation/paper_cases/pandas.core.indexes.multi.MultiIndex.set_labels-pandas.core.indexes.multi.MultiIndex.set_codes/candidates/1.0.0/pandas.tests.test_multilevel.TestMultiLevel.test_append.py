def test_append(self):
    a, b = (self.frame[:5], self.frame[5:])
    result = a.append(b)
    tm.assert_frame_equal(result, self.frame)
    result = a['A'].append(b['A'])
    tm.assert_series_equal(result, self.frame['A'])