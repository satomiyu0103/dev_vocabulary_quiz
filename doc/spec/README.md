# spec — 企画・仕様

`dev_vocabulary_quiz` の企画書・仕様の正本。

| ドキュメント | 内容 |
|---|---|
| [企画書.md](企画書.md) | 背景・目的・要件・設計・アーキテクチャ・テスト設計 |

## 関連

| パス | 役割 |
|---|---|
| [doc/agent/project-overview.md](../agent/project-overview.md) | プロジェクト概要（短縮版） |
| [CLOUDFLARE_DEPLOY.md](../../CLOUDFLARE_DEPLOY.md) | デプロイ手順 |
| `doc/life/career/dev-vocabulary/`（Documents 秘書層） | カード JSON 正本・ビルドツール |

## 作業スコープ

| フェーズ | 作業場所 |
|---|---|
| Phase 0–1 | 完了（語彙正本・テンプレ適用は Documents 横断を含む） |
| **Phase 2 以降** | **`dev_vocabulary_quiz` リポジトリ内**（本 repo を作業ルート） |

カードデータの編集正本は引き続き Documents の `doc/life/career/dev-vocabulary/`。Phase 2 以降の UI・検証・デプロイ・本 repo 内スクリプトはここで進める。

## 更新ルール

- 機能追加・モード変更・データフロー変更時は **企画書を先に更新** し、実装と差分が出ないようにする
- 現行: クイズ UI は `export/quiz.html` → `sync_to_web.ps1` で `public/` に同期。Phase 2 以降は本 repo 側への移行を検討可
