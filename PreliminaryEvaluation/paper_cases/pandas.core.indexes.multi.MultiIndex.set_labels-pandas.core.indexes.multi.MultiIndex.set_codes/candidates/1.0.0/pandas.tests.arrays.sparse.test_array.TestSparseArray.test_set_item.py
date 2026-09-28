def test_set_item(self):

    def setitem():
        self.arr[5] = 3

    def setslice():
        self.arr[1:5] = 2
    with pytest.raises(TypeError, match='assignment via setitem'):
        setitem()
    with pytest.raises(TypeError, match='assignment via setitem'):
        setslice()