# dev_vocabulary_quiz

開発語彙（schema v2）の **4 択クイズ**。Cloudflare Pages で公開する静的 Web アプリ。

## ドキュメント

| 文書 | 内容 |
|---|---|
| [doc/spec/企画書.md](doc/spec/企画書.md) | **企画書**（背景・要件・設計・アーキテクチャ・テスト） |
| [doc/spec/README.md](doc/spec/README.md) | spec 索引 |
| [doc/agent/project-overview.md](doc/agent/project-overview.md) | プロジェクト概要 |
| [CLOUDFLARE_DEPLOY.md](CLOUDFLARE_DEPLOY.md) | デプロイ手順 |

Phase 2 以降の実装は **本リポジトリ内**で行う（[企画書 §6](doc/spec/企画書.md#6-開発フェーズ)）。

## ローカル確認

```powershell
cd public
python -m http.server 8080
```

→ http://localhost:8080/
