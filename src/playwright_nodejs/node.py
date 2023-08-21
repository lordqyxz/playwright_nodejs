import logging
from pathlib import Path
from subprocess import Popen, PIPE
from typing import Union

from playwright._impl._driver import compute_driver_executable

driver_executable = compute_driver_executable()


class NodejsException(Exception):
    pass


class Nodejs:
    """represent a nodejs instance"""

    def __init__(self, source: Union[Path, str] = "", encoding: str = 'utf8', cwd=None, node_path=None):
        """
        :param source: The source code or source file path
        :param encoding: The encoding of source code
        :param cwd: Sets the current directory before the child is executed.
        :param node_path: The path of node.exe
        """
        self.logger = logging.getLogger(__name__)
        self._cwd = cwd
        self.encoding = encoding
        if isinstance(source, Path):
            self.source = source.read_text(encoding=encoding)
        elif isinstance(source, str):
            self.source = source
        else:
            raise NodejsException("The source is not source code or source file path")
        self.node_path = node_path if node_path else driver_executable.parent / 'node.exe'

    def call(self, code) -> 'Nodejs':
        """
        add a function call to source code
        :param code: the function call code
        :return: self
        """
        self.source = self.source + '\r\n' + code
        return self

    def exec(self) -> str:
        """
        run the source code
        :return: the stdout of Node.js
        """
        if not self.source:
            raise NodejsException("The source is not valid")
        p = Popen(self.node_path, stdin=PIPE, stdout=PIPE, stderr=PIPE, cwd=self._cwd, encoding=self.encoding,
                  universal_newlines=True)
        in_put = self.source
        std_out, std_err = p.communicate(input=in_put)
        ret = p.wait()
        self.logger.debug(f"nodejs return code: {ret}")
        if std_err:
            self.logger.warning(std_err)
        return std_out
