def get_result(self, buf: Optional[FilePathOrBuffer[str]]=None, encoding: Optional[str]=None) -> Optional[str]:
    """
        Perform serialization. Write to buf or return as string if buf is None.
        """
    with self.get_buffer(buf, encoding=encoding) as f:
        self.write_result(buf=f)
        if buf is None:
            return f.getvalue()
        return None