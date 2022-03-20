from __future__ import annotations

from pathlib import Path

from _pytest.fixtures import fixture


@fixture
def test_fixtures() -> TestFixtures:
    return TestFixtures()


class TestFixtures:
    @property
    def own_file_path(self) -> Path:
        return Path(__file__)

    @property
    def test_dir_path(self) -> Path:
        return self.own_file_path.parent

    @property
    def data_dir_path(self) -> Path:
        return self.test_dir_path / "data"
