def test_astype_with_view_float(self, float_frame):
    tf = np.round(float_frame).astype(np.int32)
    casted = tf.astype(np.float32, copy=False)
    tf = float_frame.astype(np.float64)
    casted = tf.astype(np.int64, copy=False)