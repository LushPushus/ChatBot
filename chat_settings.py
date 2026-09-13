import json
from pathlib import Path


SETTINGS_FILE = Path(__file__).with_name("chat_settings.json")
DEFAULT_SETTINGS = {
    "triggers": True,
}


def get_chat_settings(chat_id: int) -> dict:
    if not SETTINGS_FILE.exists():
        return DEFAULT_SETTINGS.copy()

    try:
        data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        data = {}

    settings = DEFAULT_SETTINGS.copy()
    settings.update(data.get(str(chat_id), {}))
    return settings


def set_chat_setting(chat_id: int, setting: str, value: bool) -> None:
    try:
        data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        data = {}

    data.setdefault(str(chat_id), {})[setting] = value
    SETTINGS_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
