# プロジェクト概要 — dev_vocabulary_quiz

> **要件定義**: [doc/spec/要件定義書.md](../spec/要件定義書.md) · **設計**: [設計書_基礎](../spec/設計書_基礎.md) / [詳細](../spec/設計書_詳細.md) · **テスト**: [テスト設計書](../spec/テスト設計書.md) · [doc/spec/README.md](../spec/README.md)

## 目的

開発語彙（schema v2）の 4 択クイズ。日常の学習用ブラウザアプリ。

## スコープ

| 含む | 含まない |
|---|---|
| `public/` のクイズ UI・JSON | サーバ API・ユーザー認証 |
| Cloudflare Pages デプロイ | カード編集 UI（正本は doc/life） |

## データフロー

```text
doc/life/career/dev-vocabulary/
  → sync_to_web.ps1
  → public/all_cards_v2.json + index.html
  → git commit → Cloudflare Pages
```

## デプロイ

- ホスト: Cloudflare Pages
- 出力: `public`
- 手順: [CLOUDFLARE_DEPLOY.md](../../CLOUDFLARE_DEPLOY.md)
