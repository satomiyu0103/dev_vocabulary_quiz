# Changelog

本ファイルは [Keep a Changelog](https://keepachangelog.com/ja/1.0.0/) 形式。公開 GitHub に含める。

## [Unreleased]

### Added

- `doc/life/career/dev-vocabulary/spec/解説フィールド執筆ガイド.md` — 意味/usage/コード例の執筆基準
- Phase 4 学習モード（P2 / 命名パターン / DS）を `public/index.html` に追加
- warm-palette モック準拠の UI 構造（タブ・カード・注釈・44px タップ領域）
- ルート `README.md` を本アプリ向けに復旧（sync・公開境界・デプロイ案内）
- `doc/life/career/dev-vocabulary/examples_general/` — 日常英語例文 JSON 正本（P0 97 枚）

### Changed

- カード解説品質: `card_quality.py` + `enrichment_catalog.py` でテンプレ生成廃止（anti 13 語個別・P2/DS 意味/usage 自動執筆）
- anti（単体の汎用名）の `meaning_programming_ja` を変数名・引数名・関数名の使われ方の記述に変更
- `public/index.html` — コード例 `note_ja` 表示・anti の `good_alternative` 表示
- `scripts/validate_export_json.py` — プレースホルダ・テンプレ usage 検出を追加
- `doc/life` 正本の例文品質改善（anti_pattern 全件・テンプレ例文・import のみコード例）を `sync_to_web.ps1` で同期
- `doc/spec/企画書.md` — Phase 2〜4 状態更新、Phase 5 次タスク節を追加
- 例文供給を機械テンプレ廃止 → JSON 正本 + `examples_catalog.py` に変更（未作成は「例文は準備中」）
- **全265カード**に `examples_general/` JSON 正本の例文を投入（P1 70 + P2 98 を追加）

### Added (template)

- Web 静的テンプレ agent 運用の初期構成
