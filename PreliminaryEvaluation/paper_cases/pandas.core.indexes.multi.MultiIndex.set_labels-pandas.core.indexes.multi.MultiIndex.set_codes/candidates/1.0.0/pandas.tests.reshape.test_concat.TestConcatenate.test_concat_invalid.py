def test_concat_invalid(self):
    df1 = tm.makeCustomDataframe(10, 2)
    msg = "cannot concatenate object of type '{}'; only Series and DataFrame objs are valid"
    for obj in [1, dict(), [1, 2], (1, 2)]:
        with pytest.raises(TypeError, match=msg.format(type(obj))):
            concat([df1, obj])