from typing import Any, Dict, Union

class Plan:
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def collaborators(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def private_repos(self) -> int: ...
    @property
    def space(self) -> int: ...