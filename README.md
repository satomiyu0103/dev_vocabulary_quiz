# dev_vocabulary_quiz

開発語彙（schema v2）の 4 択クイズ。Cloudflare Pages で公開する静的サイト。

## 構成

| パス | 内容 |
|---|---|
| `public/index.html` | クイズ UI（`doc/life/career/dev-vocabulary/export/quiz.html` 由来） |
| `public/all_cards_v2.json` | 265 枚統合カード |

## カード更新（正本 → 本 repo）

```powershell
# Documents ルートで
python doc/life/career/dev-vocabulary/tools/build_decks.py
python doc/life/career/dev-vocabulary/tools/validate_decks.py
powershell -NoProfile -ExecutionPolicy Bypass -File doc/life/career/dev-vocabulary/tools/sync_to_web.ps1
```

その後本 repo で commit → push → Cloudflare Pages が自動デプロイ。

## Cloudflare Pages

手順: [CLOUDFLARE_DEPLOY.md](CLOUDFLARE_DEPLOY.md)

- ビルドコマンド: なし
- 出力ディレクトリ: `public`
- フレームワーク: None

## データ正本

`doc/life/career/dev-vocabulary/`（Documents 秘書層 git）。本 repo は配信用のみ。
