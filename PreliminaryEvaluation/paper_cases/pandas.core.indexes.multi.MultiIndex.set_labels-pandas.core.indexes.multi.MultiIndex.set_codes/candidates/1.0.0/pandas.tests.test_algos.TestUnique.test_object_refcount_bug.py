def test_object_refcount_bug(self):
    lst = ['A', 'B', 'C', 'D', 'E']
    for i in range(1000):
        len(algos.unique(lst))