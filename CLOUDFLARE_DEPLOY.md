# Cloudflare Pages デプロイ手順

## 前提

- GitHub に `dev_vocabulary_quiz` リポジトリを作成済み
- Cloudflare アカウントあり

## 手順

1. 本フォルダを GitHub に push（利用者操作・承認必須）
2. [Cloudflare Dashboard](https://dash.cloudflare.com/) → Workers & Pages → Create application → Pages → Connect to Git
3. リポジトリ `dev_vocabulary_quiz` を選択
4. 設定:
   - **Build command**: （空）
   - **Build output directory**: `public`
   - **Framework preset**: None
5. Save and Deploy
6. 発行 URL（例: `https://dev-vocabulary-quiz.pages.dev`）を以下に記録:
   - `.cursor/scripts/dev-projects-manifest.json` の `deploy.url`
   - `doc/life/preferences.md`
   - Drive `03_Agent_Reference` 索引（URL のみ）

## ローカル確認

```powershell
cd public
python -m http.server 8080
```

→ http://localhost:8080/
