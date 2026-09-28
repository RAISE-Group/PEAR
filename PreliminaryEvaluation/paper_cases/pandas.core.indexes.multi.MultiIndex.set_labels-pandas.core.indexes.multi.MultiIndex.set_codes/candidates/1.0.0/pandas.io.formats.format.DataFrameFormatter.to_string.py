def to_string(self, buf: Optional[FilePathOrBuffer[str]]=None, encoding: Optional[str]=None) -> Optional[str]:
    return self.get_result(buf=buf, encoding=encoding)