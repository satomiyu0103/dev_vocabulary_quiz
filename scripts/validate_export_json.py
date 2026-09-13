"""Validate exported quiz JSON (CR-30, CR-31) before distribution."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED_CARD_FIELDS = (
    "id",
    "term",
    "meaning_general_ja",
    "meaning_programming_ja",
)
MAX_EXAMPLES_GENERAL = 3

# Mirror dev-vocabulary card_quality rules (keep in sync manually).
FORBIDDEN_USAGE_MARKERS = ("do_", "_action()")
FORBIDDEN_MEANING_PREFIX = "単体の変数名・引数名として禁止。"
PLACEHOLDER_GENERAL_PREFIXES = (
    "（専門用語",
    "（英語の",
    "（技術用語",
)


def _quality_errors(card: dict, index: int) -> list[str]:
    errors: list[str] = []
    card_id = card.get("id", f"cards[{index}]")
    mg = card.get("meaning_general_ja", "")
    if any(str(mg).startswith(prefix) for prefix in PLACEHOLDER_GENERAL_PREFIXES):
        errors.append(f"cards[{index}] ({card_id}) placeholder meaning_general_ja")
    mp = card.get("meaning_programming_ja", "")
    if str(mp).startswith(FORBIDDEN_MEANING_PREFIX):
        errors.append(f"cards[{index}] ({card_id}) templated meaning_programming_ja")
    un = card.get("usage_note_ja", "")
    if "do_" in str(un) and "_action()" in str(un):
        errors.append(f"cards[{index}] ({card_id}) do_*_action usage_note_ja")
    if un == "変数名・引数名として単体では使わない語。具体的な名前（例: parsed_json）に置き換える。":
        errors.append(f"cards[{index}] ({card_id}) duplicate anti usage_note_ja")
    for j, ex in enumerate(card.get("examples_code") or []):
        if not ex.get("note_ja"):
            errors.append(f"cards[{index}] ({card_id}) examples_code[{j}] missing note_ja")
    return errors


def validate_export(data: object) -> list[str]:
    """Return a list of validation error messages (empty if valid)."""
    errors: list[str] = []

    if not isinstance(data, dict):
        return ["root must be a JSON object"]

    cards = data.get("cards")
    if not isinstance(cards, list):
        return ["cards must be an array"]

    meta = data.get("meta")
    if not isinstance(meta, dict):
        errors.append("meta must be an object")
    else:
        card_count = meta.get("card_count")
        if card_count != len(cards):
            errors.append(
                f"meta.card_count ({card_count}) != len(cards) ({len(cards)})"
            )

    seen_ids: set[str] = set()
    for index, card in enumerate(cards):
        if not isinstance(card, dict):
            errors.append(f"cards[{index}] must be an object")
            continue

        card_id = card.get("id")
        if not card_id:
            errors.append(f"cards[{index}] missing id")
        elif card_id in seen_ids:
            errors.append(f"duplicate id: {card_id}")
        else:
            seen_ids.add(card_id)

        for field_name in REQUIRED_CARD_FIELDS:
            if field_name not in card:
                errors.append(f"cards[{index}] ({card_id}) missing {field_name}")

        examples = card.get("examples_general")
        if examples is not None:
            if not isinstance(examples, list):
                errors.append(f"cards[{index}] ({card_id}) examples_general must be array")
            elif len(examples) > MAX_EXAMPLES_GENERAL:
                errors.append(
                    f"cards[{index}] ({card_id}) examples_general exceeds {MAX_EXAMPLES_GENERAL}"
                )

        errors.extend(_quality_errors(card, index))

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python validate_export_json.py <path-to-json>", file=sys.stderr)
        return 2

    json_path = Path(sys.argv[1])
    if not json_path.is_file():
        print(f"File not found: {json_path}", file=sys.stderr)
        return 2

    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"JSON parse error: {exc}", file=sys.stderr)
        return 1

    errors = validate_export(data)
    if errors:
        print(f"Validation failed ({len(errors)} issue(s)):", file=sys.stderr)
        for message in errors:
            print(f"  - {message}", file=sys.stderr)
        return 1

    card_count = len(data["cards"]) if isinstance(data, dict) else 0
    print(f"OK: {card_count} cards, unique ids, meta.card_count consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
