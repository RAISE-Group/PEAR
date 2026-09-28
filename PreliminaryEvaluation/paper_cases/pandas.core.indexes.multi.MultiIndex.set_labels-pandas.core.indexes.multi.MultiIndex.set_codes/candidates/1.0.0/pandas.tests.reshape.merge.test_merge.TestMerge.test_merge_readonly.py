def test_merge_readonly(self):
    data1 = pd.DataFrame(np.arange(20).reshape((4, 5)) + 1, columns=['a', 'b', 'c', 'd', 'e'])
    data2 = pd.DataFrame(np.arange(20).reshape((5, 4)) + 1, columns=['a', 'b', 'x', 'y'])
    data1._data.blocks[0].values.flags.writeable = False
    data1.merge(data2)