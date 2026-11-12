# 跨領域研究生的小工具｜RL × 敗血症文獻研究助理

以固定閱讀架構整理文獻，協助跨領域研究生準備專題報告。原生 HTML/CSS/JS，無需安裝套件。

## 已有功能
文獻搜尋、分類、展開筆記、State/Action/Reward/Evaluation 導讀、七段閱讀架構、延伸閱讀、複製 AI 整理指令、規則與範本下載、手機版面。
目前三篇導讀：2018 AI Clinician（摘要層級）、2025 急診適用性（正文與圖說）、2026 時間對齊（搜尋結果層級）。並非三篇完整全文分析；範圍逐篇標示。
網站沒有內建聊天 AI、PDF 分析或自動抓文獻功能；由外部 AI 依規則協助整理，再把確認的筆記加入網站。

## 本機瀏覽
在專案目錄執行 `python3 -m http.server 8000 --directory dist`，瀏覽 http://localhost:8000 。使用伺服器才能載入 JSON。
檢查：`python3 scripts/check.py`。

## 新增內容
先讀 AGENTS.md，複製 templates/paper-template.json，填妥後加入 dist/data/papers.json 陣列。首頁由資料生成，搜尋與延伸閱讀自動更新。七段順序及資料格式由檢查程式驗證。
示範指令：請依 AGENTS.md 整理我提供的新論文，填寫範本，標記未確認資料，加入文獻庫並執行檢查。不要猜測圖表數字。

## GitHub 與公開網站
Repository：https://github.com/chientelai-max/sepsis-rl-study-desk

公開網站：https://sepsis-rl-study-desk.colorfulglint1.chatgpt.site
1. 在 GitHub 新增 public Repository，名稱 sepsis-rl-study-desk。
2. 上傳本專案內容（包含 .github/workflows/pages.yml；不要上傳 .openai/）。
3. Settings → Pages → Source 選 GitHub Actions。
4. 在 Actions 執行 Deploy GitHub Pages；成功後以實際輸出的網址為準。
5. 將真實 Repository 與網站網址填入 SUBMISSION.md。
工作流程發布 dist/，不需 npm 或打包。

## 來源與製作說明
各筆記附 DOI 原文連結。內容由 AI 協助草擬，正式報告前需人工核對原文與授權。網站未放論文全文、原圖或個案資料。原創網站結構與內容範本，非他人網站複製品。
