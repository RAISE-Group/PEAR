def write_result(self, buf: IO[str]) -> None:
    buffer_put_lines(buf, self.render())