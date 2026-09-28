def _get_subheader_index(self, signature, compression, ptype):
    index = const.subheader_signature_to_index.get(signature)
    if index is None:
        f1 = compression == const.compressed_subheader_id or compression == 0
        f2 = ptype == const.compressed_subheader_type
        if self.compression != '' and f1 and f2:
            index = const.SASIndex.data_subheader_index
        else:
            self.close()
            raise ValueError('Unknown subheader signature')
    return index