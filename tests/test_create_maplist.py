"""Test get_map_lines_created function."""

from pathlib import Path

from src.tools.addons.gets import get_map_lines_created, get_to_root


def test_create_maplist(tmp_path: Path) -> None:
    """Test get_map_lines_created function.

    Args:
        - tmp_path - built-in pytest fixture to create Pathlib temporary files

    Returns:
        None
    """
    get_to_root()
    original_maplist_path = "MapList.txt"
    d = tmp_path / "sub"
    d.mkdir()
    temp_maplist_path = d / "temp_file.txt"

    map_items = get_map_lines_created()
    with temp_maplist_path.open("w") as temp_maplist_file:
        for item in map_items:
            temp_maplist_file.write(" ".join(item) + "\n")

    with temp_maplist_path.open("r") as temp_maplist_file:
        temp_maplist = temp_maplist_file.readlines()

    with open(original_maplist_path, "r") as out_file:
        original_maplist = out_file.readlines()

    assert sorted(temp_maplist) == sorted(original_maplist)
