def _setup_build_doc(self):
    raw_text = _read(self.io)
    if not raw_text:
        raise ValueError(f'No text parsed from document: {self.io}')
    return raw_text