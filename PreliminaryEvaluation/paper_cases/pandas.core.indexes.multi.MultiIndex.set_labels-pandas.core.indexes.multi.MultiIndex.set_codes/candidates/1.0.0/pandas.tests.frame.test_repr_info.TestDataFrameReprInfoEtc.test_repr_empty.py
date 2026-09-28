def test_repr_empty(self):
    repr(DataFrame())
    frame = DataFrame(index=np.arange(1000))
    repr(frame)