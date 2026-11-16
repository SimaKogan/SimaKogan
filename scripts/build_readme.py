#!/usr/bin/env python3
"""Генерирует README.md из README.template.md и profile.json.

Использование:
    cp profile.example.json profile.json   # впиши свои данные
    python scripts/build_readme.py         # создаст README.md
"""
import json
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent

SOCIALS = {
    # ключ: (подпись, иконка simpleicons, цвет, шаблон ссылки)
    "linkedin": ("LinkedIn", "linkedin", "0A66C2", "https://linkedin.com/in/{}"),
    "telegram": ("Telegram", "telegram", "26A5E4", "https://t.me/{}"),
    "instagram": ("Instagram", "instagram", "E4405F", "https://instagram.com/{}"),
    "twitter": ("X", "x", "000000", "https://x.com/{}"),
    "email": ("Email", "gmail", "EA4335", "mailto:{}"),
    "website": ("Website", "googlechrome", "7C3AED", "{}"),
}


def build_badges(username: str, socials: dict) -> str:
    gh = username.replace("-", "--")
    items = [
        f'<a href="https://github.com/{username}"><img src="https://img.shields.io/badge/GitHub-{gh}-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>'
    ]
    for key, (label, icon, color, link) in SOCIALS.items():
        value = (socials.get(key) or "").strip()
        if not value:
            continue
        items.append(
            f'<a href="{link.format(value)}"><img src="https://img.shields.io/badge/{label}-{color}?style=for-the-badge&logo={icon}&logoColor=white" alt="{label}"/></a>'
        )
    return "\n".join(items)


def main() -> None:
    cfg_path = ROOT / "profile.json"
    if not cfg_path.exists():
        sys.exit("Не найден profile.json — скопируй profile.example.json и заполни.")
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))

    name, user = cfg["name"], cfg["username"]
    values = {
        "NAME_URL": quote(name),
        "ROLE_URL": quote(cfg.get("role", "")),
        "USERNAME": user,
        "TAGLINES_URL": ";".join(quote(t) for t in cfg.get("taglines", [name])),
        "SOCIAL_BADGES": build_badges(user, cfg.get("socials", {})),
        "ABOUT": "\n".join(f"- {line}" for line in cfg.get("about", [])),
        "SKILLS": ",".join(cfg.get("skills", [])),
    }

    text = (ROOT / "README.template.md").read_text(encoding="utf-8")
    for key, val in values.items():
        text = text.replace("{{" + key + "}}", val)

    (ROOT / "README.md").write_text(text, encoding="utf-8")
    print("README.md создан ✔")


if __name__ == "__main__":
    main()
