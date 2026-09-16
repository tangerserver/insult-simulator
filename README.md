# 嘴臭模擬器 (Insult Simulator)

Reddit 式發洩工具？不需要——直接罵這個機器人！你想怎麼罵都可以，它會**火力全開回嗆**，越罵越兇，不會投降。

支援 **Windows / iOS（網頁版）** 與 **macOS / Linux（桌面版）**。

## 玩法

1. 開啟網頁或下載桌面版
2. 盡情輸入髒話、辱罵、嘲諷——想罵什麼就罵什麼
3. 系統會依序**升級回嗆**（冷嘲 → 嘲諷 → 狠嗆 → 火力全開）
4. 它的**怒氣值**會一直漲，但永遠不會投降 🖕

## 使用方式

| 平台 | 用法 | 說明 |
|------|------|------|
| **Windows** | **網頁版** | 直接開瀏覽器用，免安裝、免下載（避免 SmartScreen「不明的開發者」警告） |
| **iOS / 手機** | **網頁版** | 用 Safari 開啟，可「加入主畫面」當 App 用 |
| macOS | `InsultSimulator-macOS.zip` | 桌面版，解壓後拖入「應用程式」資料夾 |
| Linux | `InsultSimulator-Linux.zip` | 桌面版，64 位元，需安裝 WebKit2GTK |

**網頁版（Windows / iOS 通用）**：[https://tangerserver.github.io/insult-simulator/](https://tangerserver.github.io/insult-simulator/)

> 說明：Windows 與 iOS 直接用網頁版即可，無需下載安裝；網頁版與桌面版玩法完全相同。

## 系統需求（桌面版）

### macOS
- macOS 11.0 以上

### Linux
- 64 位元 Linux，需安裝 WebKit2GTK：
  - Debian/Ubuntu：`sudo apt install libwebkit2gtk-4.1-0`
  - Fedora：`sudo dnf install pango gdk-pixbuf2 libnotify webkit2gtk4.1`

## 注意

- 本程式僅為娛樂用途，所有回嗆言論不代表任何立場
- 遊戲目的在於以輕鬆方式宣洩壓力，請勿在現實中仿照（當然，這大家都知道 😐）

## 開發建置

- 桌面版使用 [pywebview](https://github.com/r0x0r/pywebview) + PyInstaller，跨平台由 GitHub Actions 自動編譯
- 網頁版為單一 `docs/index.html`，可自行在瀏覽器開啟

## 授權

僅供個人娛樂與學習使用。