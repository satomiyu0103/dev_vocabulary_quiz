---
name: dev-vocabulary-quiz-design-system
description: 開発語彙 4 択クイズのデザイン正本。カジュアル・視覚過敏・色弱配慮の配色とコンポーネント。
colors:
  background-primary: "#FAFAF8"
  background-secondary: "#EDECEA"
  accent-primary: "#2B6CB0"
  accent-primary-hover: "#245A92"
  accent-tint: "#E8F0FA"
  text-primary: "#1A2332"
  text-secondary: "#4A5568"
  border-subtle: "#C8CDD4"
  success: "#0D6E6E"
  success-bg: "#E6F4F1"
  error: "#B45309"
  error-bg: "#FEF3E6"
  info: "#5C6B7A"
typography:
  display: "Hiragino Sans"
  body: "Hiragino Sans, Yu Gothic UI, Segoe UI, sans-serif"
  mono: "ui-monospace, Consolas, monospace"
---

# Design System: 開発語彙 4 択クイズ

**Project ID:** なし

> ビジュアル正本。実装は [`public/index.html`](public/index.html) の CSS 変数へ反映する（反映前は本書のトークンを優先）。
> 機能・画面の正本: [doc/spec/設計書_基礎.md](doc/spec/設計書_基礎.md) · [doc/spec/設計書_詳細.md](doc/spec/設計書_詳細.md)

---

## 1. Visual Theme & Atmosphere

移動中やすきま時間に、サクッと英単語を復習するための **カジュアルな 4 択クイズ**。堅い「学習システム」ではなく、気楽に開いて 1 問ずつ進められる雰囲気を目指す。

配色は眩しすぎないオフホワイトと落ち着いた青を基調にし、**視覚過敏**（まぶしさ・刺激への敏感さ）と **色弱**（赤と緑の区別が難しいなど）に配慮する。正解・不正解は色だけに頼らず、文言と枠のスタイルで伝える（要件 NFR-20）。

**Key Characteristics:**

- 1 カラム・最大幅 640px — スマホ片手操作向け
- 余白多め・フラット UI — 強い影・グラデ・点滅なし
- カジュアルなです・ます調の文言 — 堅い管理画面感を避ける
- 正誤は **【結果】正解！／不正解** の文字を主役 — 色は補助
- アクセントは青系に統一 — 赤 vs 緑の二色だけで状態を分けない

**利用シーン:** 電車・バスでの暇つぶし、実装前のウォームアップ、コードを読むときの語彙想起。

---

## 2. Color Palette & Roles

### Primary Foundation

- **Soft Mist Gray** (#EDECEA) – ページ背景（`background-secondary`）。純白より眩しくない温かみのあるグレー。
- **Warm Paper White** (#FAFAF8) – カード・パネル（`background-primary`）。`#FFFFFF` 全面は使わない。

### Accent & Interactive

- **Calm Study Blue** (#2B6CB0) – プライマリ CTA・アクティブなモード・リンク（`accent-primary`）。
- **Deeper Study Blue** (#245A92) – hover・押下時（`accent-primary-hover`）。
- **Light Blue Wash** (#E8F0FA) – 選択肢 hover・トップリンク背景（`accent-tint`）。装飾用の低彩度。

### Typography & Text Hierarchy

- **Ink Navy** (#1A2332) – 見出し・本文・4 択ラベル（`text-primary`）。真っ黒 `#000000` は使わない。
- **Slate Caption** (#4A5568) – サブタイトル・統計・補足（`text-secondary`）。
- **Gentle Line Gray** (#C8CDD4) – パネル・ボタン枠（`border-subtle`）。

### Functional States

正誤・注意は **色＋文言＋枠スタイル** の三つ組。色だけで伝えない（NFR-20）。

| トークン | 描写名 | HEX | 用途 |
|---|---|---|---|
| `success` | Confident Teal | #0D6E6E | 正解の補助（枠・文字の一部） |
| `success-bg` | Mint Whisper | #E6F4F1 | 正解選択肢の背景 |
| `error` | Warm Amber Alert | #B45309 | 不正解の補助（赤ではなく橙系） |
| `error-bg` | Peach Whisper | #FEF3E6 | 不正解選択肢の背景 |
| `info` | Neutral Hint | #5C6B7A | 読み込みヒント・中立メッセージ |

**非推奨（現行実装に残る場合の置き換え目安）:** 鮮やかな赤 `#9F1F16` と緑 `#0A6B40` の **ペアのみ** で正誤を表すデザイン。

### Accessibility（色弱・視覚過敏）

| Do | Don't |
|---|---|
| 正誤に「正解」「不正解」の文言を必ず付ける | 赤と緑の背景色だけで正誤を区別する |
| ページ背景は #EDECEA など低輝度 | 全面 `#FFFFFF` や高彩度の原色背景 |
| 正解は実線の太枠（2px）+ ティール系 | 緑一色に依存 |
| 不正解は破線枠（2px）+ 橙系 | 赤一色に依存 |
| アニメーションは 150ms 以内の色変化のみ | 点滅・パララックス・強い pulse |
| モード active は青系 `accent-primary` | 赤/緑でモードや進捗を色分け |

### Contrast Targets（NFR-21）

WCAG 2.1 AA 目安（4.5:1 以上）。実装反映時にツールで再確認する。

| 前景 | 背景 | 用途 | 目標 |
|---|---|---|---|
| #1A2332 | #FAFAF8 | 本文・4 択 | ≥ 4.5:1 |
| #1A2332 | #EDECEA | 本文 on ページ | ≥ 4.5:1 |
| #4A5568 | #FAFAF8 | 補足・統計 | ≥ 4.5:1 |
| #FFFFFF | #2B6CB0 | CTA ボタン文字 | ≥ 4.5:1 |
| #0D6E6E | #E6F4F1 | 正解状態（補助） | 文言が主。色は補助 |

---

## 3. Typography Rules

**Primary Font Family:** `"Hiragino Sans", "Yu Gothic UI", "Segoe UI", sans-serif`  
**Character:** 角の立ちすぎないゴシック。和文を主に、英単語・コードは同ファミリーで統一。Web フォントの追加読み込みはしない（軽量配信）。

**Code / Mono:** `ui-monospace, Consolas, monospace` — コード例ブロックのみ。

### Hierarchy & Weights

| 用途 | サイズ | ウェイト | 行間 | 使用箇所 |
|---|---|---|---|---|
| Display (H1) | 1.5rem | 700 | 1.3 | アプリ名「開発語彙 4 択クイズ」 |
| Subtitle | 1rem | 400 | 1.65 | `.sub` サブタイトル |
| Question Label | 1.05rem | 700 | 1.4 | `#q-label` 問題番号・モード |
| Prompt | 1.05rem | 700 | 1.4 | 「次の説明に合う英単語はどれ？」 |
| Meaning Block | 1.05rem | 500 | 1.65 | `#q-general`, `#q-prog` |
| Choice / Button | 1.05rem | 500 | 1.65 | 4 択・モードボタン |
| Result Line | 1.25rem | 800 | 1.3 | `#result-line` 正誤（文言必須） |
| Explain DT | 0.95rem | 700 | 1.4 | 解説見出し |
| Explain DD | 1.02rem | 400 | 1.65 | 解説本文 |
| Small / Meta | 0.85rem | 400 | 1.65 | `#stats`, `#load-hint` |
| CTA Label | 1rem | 600 | 1.4 | 「次の問題」 |

### Spacing Principles

- 見出しとサブタイトル: 0.35rem〜0.75rem
- 意味ブロック間: 0.5rem
- 4 択グリッド gap: 0.5rem
- パネル間: 1rem
- パネル内 padding: 1rem〜1.25rem

---

## 4. Component Stylings

### Panel（`.panel`）

- **Background:** Warm Paper White (#FAFAF8)
- **Border:** 1px solid Gentle Line Gray (#C8CDD4)
- **Corner:** 10px
- **Shadow:** なし（フラット）
- **Padding:** 1rem 1.25rem

### ModeButton（`.mode`）

- **Default:** 白背景、1px `#C8CDD4` 枠、padding 0.55rem 0.9rem、角 8px
- **Active:** 背景 Calm Study Blue (#2B6CB0)、文字 #FFFFFF、枠同色
- **Hover（非 active）:** 背景 Light Blue Wash (#E8F0FA)
- **Focus:** `:focus-visible` — 2px solid #2B6CB0、outline-offset 2px

### ChoiceButton（`.choice`）

- 全幅・左揃え・min-height **44px**（タップ領域）
- **Default:** 白背景、1px `#C8CDD4`
- **Hover（未回答）:** 背景 `#E8F0FA`
- **Correct（回答後）:** 背景 Mint Whisper (#E6F4F1)、枠 **2px solid** Confident Teal (#0D6E6E)。文言で「正解」が既に `#result-line` にあること
- **Wrong（回答後）:** 背景 Peach Whisper (#FEF3E6)、枠 **2px dashed** Warm Amber Alert (#B45309)
- **Disabled:** opacity 0.5

### PrimaryCTA（`.primary` / `#next-btn`）

- 背景 #2B6CB0、文字 #FFFFFF、全幅、角 8px、padding 0.55rem 0.9rem、font-weight 600
- margin-top 0.75rem
- **Focus:** 同上 2px outline

### MeaningBlock（`#q-general`, `#q-prog`）

- 背景 `#F3F6FA`（意味ブロック用のごく薄い青灰）
- 左ボーダー **4px solid** #2B6CB0
- padding 0.65rem 0.75rem、角 4px

### ResultLine（`#result-line`）

- **必須文言:** `【結果】正解！` または `【結果】不正解（正解は X）`
- **Correct class:** 文字色 Confident Teal (#0D6E6E)。色盲モードでも文言で判別可能
- **Wrong class:** 文字色 Warm Amber Alert (#B45309)
- 装飾アイコン（○/×）は任意。あっても文言は省略しない

### ExplainDL（`.explain` / `#explain`）

- `dt`: font-weight 700、#1A2332、margin-top 0.75rem
- `dd`: margin 0.2rem 0 0
- **CR-20 見出し（固定）:** 「コードもしくはプログラミングでの使われ方」
- コード例 `code`: 背景 `#E8ECF2`、padding 0.5rem 0.65rem、角 6px、pre-wrap

### TopLink（`#top-link`）

- 色 #2B6CB0、font-weight 600、padding 0.35rem 0.5rem、角 6px
- hover 背景 #E8F0FA

### Setup（`#setup`）

- ファイル選択ボタンは ModeButton と同スタイル
- `#load-hint`: text-secondary、0.9rem

### Focus（共通・NFR-22）

```css
button:focus-visible,
a:focus-visible,
.choice:focus-visible {
  outline: 2px solid #2B6CB0;
  outline-offset: 2px;
}
```

### Motion

- transition: `background 0.15s ease`, `border-color 0.15s ease` のみ
- 点滅・scale アニメーション禁止

---

## 5. Layout Principles

### Grid & Structure

- **Max Content Width:** 640px（`main { max-width: 640px; margin: 0 auto; }`）
- **Grid:** 1 カラム。4 択は CSS Grid `gap: 0.5rem` 縦並び
- **Breakpoints:**
  - Mobile: 〜767px（主ターゲット・360px 幅で確認）
  - Tablet / Desktop: 768px〜（同一 1 カラム。横に広げない）

### Whitespace Strategy

- **Base unit:** 8px
- **Body padding:** 1rem
- **Component spacing:** 0.5rem〜1rem
- **Section（パネル間）:** 1rem

### Alignment & Responsive

- **Text alignment:** 左揃え（4 択・意味ブロック）
- **Touch targets:** 最小 44×44 CSS px（padding 込み）
- **Mobile-first:** 常に 1 カラム。モードバーは `flex-wrap` で折り返し

---

## 6. Notes for AI / Stitch Generation

### Atmosphere (一行)

> Casual, calm vocabulary quiz with soft off-white backgrounds, blue accents, and clear text-first feedback — accessible for color vision deficiency and light sensitivity.

### Color References (コピペ用)

- Page background: Soft Mist Gray (#EDECEA)
- Card: Warm Paper White (#FAFAF8)
- Text: Ink Navy (#1A2332)
- Accent / CTA: Calm Study Blue (#2B6CB0)
- Correct assist: Confident Teal (#0D6E6E) on Mint Whisper (#E6F4F1)
- Wrong assist: Warm Amber Alert (#B45309) on Peach Whisper (#FEF3E6)

### Component Prompts (例)

- "Primary button: Calm Study Blue (#2B6CB0) background, white text, 8px rounded corners, full width on mobile"
- "Quiz choice card: white background, gentle gray border, 44px min height, left-aligned label"
- "Correct state: mint whisper background, 2px solid teal border — always pair with the word 正解 in text"
- "Wrong state: peach whisper background, 2px dashed amber border — always pair with 不正解 in text"

### Do / Don't

- **Do:** 描写名 + hex、役割の明示、余白、文言での正誤、青系アクセント
- **Don't:** 赤と緑だけで正誤、全面純白、強い影・グラデ、点滅、堅いビジネス UI トーン
- **Don't:** フレームワーククラス名だけをプロンプトの主語にしない（`rounded-lg` 等）

### CSS Variable Mapping（実装時）

| DESIGN トークン | 推奨 CSS 変数 |
|---|---|
| `background-secondary` | `--bg` |
| `background-primary` | `--card` |
| `text-primary` | `--text` |
| `text-secondary` | `--muted` |
| `accent-primary` | `--accent` |
| `accent-tint` | `--accent-tint` |
| `border-subtle` | `--border` |
| `success` | `--ok` |
| `success-bg` | `--ok-bg` |
| `error` | `--bad` |
| `error-bg` | `--bad-bg` |

詳細: [doc/spec/設計書_詳細.md](doc/spec/設計書_詳細.md) §7.2

---

*Last updated: 2026-09-06 — v1.0 カジュアル・視覚過敏・色弱配慮パレット。クイズ向け全文充填。*
