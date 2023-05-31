from __future__ import annotations
from typing import List, Any


class Structure:
    """
    Represents a database tabel structure.

    Attributes
    ----------
    name: str
        The name of the specific structure.
    id: int
        The autogenerated 16 digit integer used
        for the structure
    data_type: Any
        The data_type that is contained within
        the structure.
    """

    name: str
    id: int
    data_type: Any


class Entry:
    """
    Represents a database entry.

    Attributes
    ----------
    value: str
        The value of the entry.
    table: Table
        The table the entry is inside.
    """

    value: str
    table: Table


class Table:
    """
    Represents a database table.

    Attributes
    ----------
    name: str
        The name of the table.
    id: int
        The id of the table.
    structure: List[Structure]
        The table structure.
    rows: List[Entry]
    """

    name: str
    id: int
    structure: List[Structure]
    rows: List[Entry]

    async def delete(self) -> bool:
        ...

    async def rename(self) -> bool:
        ...
