from dataclasses import dataclass
from logging import Logger
from pathlib import Path
from typing import List

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Document:
    body: str  # Should be the longest string field


@dataclass_json
@dataclass
class Documents:
    list_document: List[Document]


class DocumentsDataSet:
    def __init__(self, filepath: Path, logger: Logger) -> None:
        self.filepath = filepath
        self.logger = Logger
