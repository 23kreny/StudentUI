from pathlib import Path

conf_dir = Path.home().joinpath(".studentui")
auth_file = conf_dir.joinpath("auth.json")

if not conf_dir.is_dir():
    conf_dir.mkdir()
