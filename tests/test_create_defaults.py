"""Test get_js_lines, get_lua_lines and get_settings functions."""

from filecmp import cmp
from pathlib import Path

from src.tools.addons.gets import get_js_lines, get_lua_lines, get_settings, get_to_root


def test_create_defaults(tmp_path: Path) -> None:
    """Test Test get_js_lines, get_lua_lines and get_settings functions.

    Args:
        - tmp_path - built-in pytest fixture to create Pathlib temporary files

    Returns:
        None
    """
    get_to_root()
    original_lua_path = "ext/Shared/Languages/DEFAULT.lua"
    d = tmp_path / "sub"
    d.mkdir()
    temp_lua_path = d / "temp_file.lua"

    all_settings = get_settings(first_key="Text")
    with temp_lua_path.open("a") as temp_lua:
        temp_lua.write(
            "local code = 'xx_XX' -- Add/replace the xx_XX here with your language code (like de_DE, en_US, or other)!\n\n"
        )
        out_file_lines = get_lua_lines(all_settings)
        for line in out_file_lines:
            temp_lua.write(line + "\n")

    original_js_path = "WebUI/languages/DEFAULT.js"
    temp_js_path = d / "temp_file.js"

    with temp_js_path.open("a") as temp_js:
        temp_js.write(
            """Language['xx_XX'] /* Add/replace the xx_XX here with your language code (like de_DE, en_US, or other)! */ = {
	"__LANGUAGE_INFO": {
		"name": "English",
		"author": "Unknown",
		"version": "1.0.0"
	},
"""
        )
        out_file_lines = get_js_lines()
        for translation in out_file_lines:
            temp_js.write('	"' + translation + '": "",\n')
        temp_js.write("};")

    assert cmp(f"{d}/temp_file.lua", original_lua_path)
    assert cmp(f"{d}/temp_file.js", original_js_path)
