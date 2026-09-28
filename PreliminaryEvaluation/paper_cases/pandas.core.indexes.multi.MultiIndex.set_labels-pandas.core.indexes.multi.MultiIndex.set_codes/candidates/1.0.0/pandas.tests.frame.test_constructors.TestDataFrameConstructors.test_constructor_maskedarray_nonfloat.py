def test_constructor_maskedarray_nonfloat(self):
    mat = ma.masked_all((2, 3), dtype=int)
    frame = DataFrame(mat, columns=['A', 'B', 'C'], index=[1, 2])
    assert len(frame.index) == 2
    assert len(frame.columns) == 3
    assert np.all(~np.asarray(frame == frame))
    frame = DataFrame(mat, columns=['A', 'B', 'C'], index=[1, 2], dtype=np.float64)
    assert frame.values.dtype == np.float64
    mat2 = ma.copy(mat)
    mat2[0, 0] = 1
    mat2[1, 2] = 2
    frame = DataFrame(mat2, columns=['A', 'B', 'C'], index=[1, 2])
    assert 1 == frame['A'][1]
    assert 2 == frame['C'][2]
    mat = ma.masked_all((2, 3), dtype='M8[ns]')
    frame = DataFrame(mat, columns=['A', 'B', 'C'], index=[1, 2])
    assert len(frame.index) == 2
    assert len(frame.columns) == 3
    assert isna(frame).values.all()
    frame = DataFrame(mat, columns=['A', 'B', 'C'], index=[1, 2], dtype=np.int64)
    assert frame.values.dtype == np.int64
    mat2 = ma.copy(mat)
    mat2[0, 0] = 1
    mat2[1, 2] = 2
    frame = DataFrame(mat2, columns=['A', 'B', 'C'], index=[1, 2])
    assert 1 == frame['A'].view('i8')[1]
    assert 2 == frame['C'].view('i8')[2]
    mat = ma.masked_all((2, 3), dtype=bool)
    frame = DataFrame(mat, columns=['A', 'B', 'C'], index=[1, 2])
    assert len(frame.index) == 2
    assert len(frame.columns) == 3
    assert np.all(~np.asarray(frame == frame))
    frame = DataFrame(mat, columns=['A', 'B', 'C'], index=[1, 2], dtype=object)
    assert frame.values.dtype == object
    mat2 = ma.copy(mat)
    mat2[0, 0] = True
    mat2[1, 2] = False
    frame = DataFrame(mat2, columns=['A', 'B', 'C'], index=[1, 2])
    assert frame['A'][1] is True
    assert frame['C'][2] is False