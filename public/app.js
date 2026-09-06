/**
 * サンプルアプリ — テンプレの命名・コメント見本。
 * 処理の大枠: ページ読み込み後にステータス文言を表示する。
 */

/**
 * ステータス文言を画面に表示する。
 * 受け取る: 表示する文字列
 * 処理の流れ: 1) DOM 要素を取得 2) textContent で安全に表示
 */
function renderStatusMessage(statusText) {
  const statusMessageElement = document.getElementById("status-message");
  if (!statusMessageElement) {
    return;
  }
  statusMessageElement.textContent = statusText;
}

document.addEventListener("DOMContentLoaded", () => {
  renderStatusMessage("Replace this page with your app.");
});
