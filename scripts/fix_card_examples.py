#!/usr/bin/env python3
"""Fix templated examples in all_cards_v2.json: dedupe ids, natural anti_pattern sentences, code usage."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "public" / "all_cards_v2.json"

ANTI_PATTERN_EXAMPLES: dict[str, list[dict[str, str]]] = {
    "temp": [
        {"en": "The temp dropped below freezing last night.", "ja": "昨晩、気温が氷点下まで下がった。"},
        {"en": "She works as a temp at the front desk.", "ja": "彼女は受付で臨時社員として働いている。"},
        {"en": "Save drafts in a temp folder first.", "ja": "まず一時フォルダに下書きを保存する。"},
    ],
    "payload": [
        {"en": "The rocket carried a heavy payload into orbit.", "ja": "ロケットは重い積載物を軌道に運んだ。"},
        {"en": "Reduce the payload size before you send the request.", "ja": "リクエストを送る前にペイロードのサイズを小さくする。"},
        {"en": "Each truck has a maximum payload limit.", "ja": "各トラックには最大積載量の上限がある。"},
    ],
    "count": [
        {"en": "We did a quick count of the chairs.", "ja": "椅子をざっと数えた。"},
        {"en": "The word count must stay under 500.", "ja": "語数は500以内に収める必要がある。"},
        {"en": "Hold the button for a five-second count.", "ja": "ボタンを5秒間押し続ける。"},
    ],
    "result": [
        {"en": "The election result surprised everyone.", "ja": "選挙の結果は誰もが驚いた。"},
        {"en": "What was the result of your blood test?", "ja": "血液検査の結果はどうだった？"},
        {"en": "Hard work usually leads to a good result.", "ja": "努力はたいてい良い結果につながる。"},
    ],
    "handle": [
        {"en": "Please handle this package with care.", "ja": "この荷物は丁寧に扱ってください。"},
        {"en": "She knows how to handle difficult customers.", "ja": "彼女は難しい客への対応がうまい。"},
        {"en": "Turn the handle to open the door.", "ja": "ドアを開けるには取っ手を回す。"},
    ],
    "process": [
        {"en": "Learning a language is a slow process.", "ja": "言語を学ぶのは時間のかかる過程だ。"},
        {"en": "The hiring process takes about two weeks.", "ja": "採用の手続きは約2週間かかる。"},
        {"en": "We need to process these forms today.", "ja": "今日中にこれらの書類を処理する必要がある。"},
    ],
    "node": [
        {"en": "Each node in the network can fail independently.", "ja": "ネットワークの各ノードは独立して故障しうる。"},
        {"en": "The diagram shows a node connected to three others.", "ja": "図には3つと接続されたノードが示されている。"},
        {"en": "Remove the swollen lymph node only if necessary.", "ja": "必要な場合だけ腫れたリンパ節を取り除く。"},
    ],
    "line": [
        {"en": "Please wait in line at the counter.", "ja": "カウンターで列に並って待ってください。"},
        {"en": "Draw a straight line between the two points.", "ja": "2点の間にまっすぐな線を引く。"},
        {"en": "The opening line of the novel is famous.", "ja": "その小説の冒頭の一文は有名だ。"},
    ],
    "value": [
        {"en": "This ring has great sentimental value.", "ja": "この指輪には大きな感情的な価値がある。"},
        {"en": "Enter a numeric value in the form field.", "ja": "フォームの欄に数値を入力する。"},
        {"en": "The value of education is hard to measure.", "ja": "教育の価値は測りにくい。"},
    ],
    "info": [
        {"en": "I left more info in the email.", "ja": "詳しい情報はメールに書いた。"},
        {"en": "The tourist office has maps and other info.", "ja": "観光案内所には地図などの情報がある。"},
        {"en": "Call this number for flight info.", "ja": "便の情報はこの番号に電話する。"},
    ],
    "item": [
        {"en": "Each item on the menu costs under ten dollars.", "ja": "メニューの各品は10ドル未満だ。"},
        {"en": "Check every item on the shopping list.", "ja": "買い物リストの品目をすべて確認する。"},
        {"en": "This item is out of stock right now.", "ja": "この商品は今在庫切れだ。"},
    ],
}

IMPORT_ONLY_RE = re.compile(r"^from\s+\S+\s+import\s+.+$|^import\s+\S+\s*$")

CODE_SNIPPET_FIXES: dict[str, list[str]] = {
    "from openpyxl import load_workbook": [
        'wb = load_workbook("report.xlsx")',
        'sheet = wb.active',
        'sheet["A1"] = "updated"',
    ],
    "from selenium import webdriver": [
        "driver = webdriver.Chrome()",
        'driver.get("https://example.com")',
        "driver.quit()",
    ],
    "from pynput import keyboard": [
        "listener = keyboard.Listener(on_press=on_key_press)",
        "listener.start()",
        "listener.stop()",
    ],
    "from sklearn.model_selection import train_test_split": [
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)",
    ],
    "from dotenv import load_dotenv": [
        "load_dotenv()",
        'api_key = os.getenv("API_KEY")',
    ],
    "from hakata_gym_crowding.config import": [
        "from hakata_gym_crowding.config import Settings",
        "settings = Settings.from_env()",
    ],
}


def is_templated_general_example(sentence: str) -> bool:
    return " is on the table." in sentence or "We need a new " in sentence or "Check the " in sentence and " first." in sentence


def build_identifier_examples(card: dict) -> list[dict[str, str]]:
    term = card.get("term", "")
    meaning = card.get("meaning_general_ja", "")
    word_class = card.get("word_class", "noun")

    if word_class == "verb":
        return [
            {"en": f"Please {term} the report by Friday.", "ja": f"金曜までにレポートを{meaning}してください。"},
            {"en": f"I will {term} it after lunch.", "ja": f"昼食後にそれを{meaning}します。"},
            {"en": f"Can you {term} this file for me?", "ja": f"このファイルを{meaning}してくれますか？"},
        ]

    return [
        {"en": f"Review the {term} before the meeting.", "ja": f"会議の前に{term}を確認する。"},
        {"en": f"The {term} was updated this morning.", "ja": f"今朝{term}が更新された。"},
        {"en": f"Open the latest {term} from the shared folder.", "ja": f"共有フォルダから最新の{term}を開く。"},
    ]


def fix_identifier_card(card: dict) -> bool:
    if card.get("type") != "identifier":
        return False
    examples = card.get("examples_general") or []
    if not any(is_templated_general_example(ex.get("en", "")) for ex in examples):
        return False
    card["examples_general"] = build_identifier_examples(card)
    return True


def fix_anti_pattern_card(card: dict) -> bool:
    if card.get("type") != "anti_pattern":
        return False
    term = card.get("term", "")
    if term not in ANTI_PATTERN_EXAMPLES:
        return False
    examples = card.get("examples_general") or []
    if not any(is_templated_general_example(ex.get("en", "")) for ex in examples):
        return False
    card["examples_general"] = ANTI_PATTERN_EXAMPLES[term]
    return True


def fix_code_examples(card: dict) -> bool:
    changed = False
    code_examples = card.get("examples_code") or []
    for index, example in enumerate(code_examples):
        snippet = (example.get("snippet") or "").strip()
        if not snippet:
            continue
        if snippet in CODE_SNIPPET_FIXES:
            replacements = CODE_SNIPPET_FIXES[snippet]
            example["snippet"] = replacements[min(index, len(replacements) - 1)]
            changed = True
        elif IMPORT_ONLY_RE.match(snippet) and snippet not in CODE_SNIPPET_FIXES:
            package_name = card.get("term", "module")
            example["snippet"] = f"# use {package_name} after import — see usage_note_ja"
            changed = True
    return changed


def dedupe_cards(cards: list[dict]) -> list[dict]:
    seen: set[str] = set()
    unique: list[dict] = []
    for card in cards:
        card_id = card["id"]
        if card_id in seen:
            continue
        seen.add(card_id)
        unique.append(card)
    return unique


def main() -> int:
    json_path = JSON_PATH
    if len(sys.argv) > 1:
        json_path = Path(sys.argv[1])

    payload = json.loads(json_path.read_text(encoding="utf-8"))
    cards = payload.get("cards", [])

    before_count = len(cards)
    cards = dedupe_cards(cards)
    anti_fixed = sum(1 for card in cards if fix_anti_pattern_card(card))
    identifier_fixed = sum(1 for card in cards if fix_identifier_card(card))
    code_fixed = sum(1 for card in cards if fix_code_examples(card))

    payload["cards"] = cards
    payload.setdefault("meta", {})
    payload["meta"]["card_count"] = len(cards)

    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"cards: {before_count} -> {len(cards)} (deduped {before_count - len(cards)})")
    print(f"anti_pattern examples fixed: {anti_fixed}")
    print(f"identifier examples fixed: {identifier_fixed}")
    print(f"code examples touched: {code_fixed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
