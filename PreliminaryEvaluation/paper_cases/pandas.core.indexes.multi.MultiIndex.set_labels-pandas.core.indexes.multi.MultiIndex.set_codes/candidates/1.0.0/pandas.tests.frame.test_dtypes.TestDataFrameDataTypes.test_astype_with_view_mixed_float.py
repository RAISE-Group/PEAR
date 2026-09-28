def test_astype_with_view_mixed_float(self, mixed_float_frame):
    tf = mixed_float_frame.reindex(columns=['A', 'B', 'C'])
    casted = tf.astype(np.int64)
    casted = tf.astype(np.float32)