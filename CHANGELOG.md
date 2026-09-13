# Changelog

本ファイルは [Keep a Changelog](https://keepachangelog.com/ja/1.0.0/) 形式。公開 GitHub に含める。

## [Unreleased]

### Added

- Phase 4 学習モード（P2 / 命名パターン / DS）を `public/index.html` に追加
- warm-palette モック準拠の UI 構造（タブ・カード・注釈・44px タップ領域）
- ルート `README.md` を本アプリ向けに復旧（sync・公開境界・デプロイ案内）
- `doc/life/career/dev-vocabulary/examples_general/` — 日常英語例文 JSON 正本（P0 97 枚）

### Changed

- `doc/life` 正本の例文品質改善（anti_pattern 全件・テンプレ例文・import のみコード例）を `sync_to_web.ps1` で同期
- `doc/spec/企画書.md` — Phase 2〜4 状態更新、Phase 5 次タスク節を追加
- 例文供給を機械テンプレ廃止 → JSON 正本 + `examples_catalog.py` に変更（未作成は「例文は準備中」）
- **全265カード**に `examples_general/` JSON 正本の例文を投入（P1 70 + P2 98 を追加）

### Added (template)

- Web 静的テンプレ agent 運用の初期構成
