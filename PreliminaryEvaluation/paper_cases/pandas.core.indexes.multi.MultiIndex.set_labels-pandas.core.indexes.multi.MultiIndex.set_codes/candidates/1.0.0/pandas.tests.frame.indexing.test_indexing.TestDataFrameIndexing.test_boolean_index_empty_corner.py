def test_boolean_index_empty_corner(self):
    blah = DataFrame(np.empty([0, 1]), columns=['A'], index=DatetimeIndex([]))
    k = np.array([], bool)
    blah[k]
    blah[k] = 0