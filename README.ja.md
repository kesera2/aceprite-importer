![Aseprite Importer](aseprite-importer-logo.gif)

<div align="right">

[English](README.md) | [日本語](README.ja.md)

</div>

# 🎨 Aseprite Importer for Blender

✨ AsepriteファイルをBlenderにピクセルメッシュとしてインポートし、Solidifyモディファイアを適用します。

## ⭐ 機能

- 📥 `.aseprite`ファイルを直接Blenderにインポート
- 🎲 ピクセルアートを自動的に3Dメッシュに変換
- 📦 3Dの厚みを出すためにSolidifyモディファイアを適用
- 🖼️ ピクセルパーフェクトなテクスチャを適切なUVマッピングで保持
- 🪄 透明なピクセルはメッシュ生成から除外

## 💾 インストール

1. 📦 最新リリースをダウンロード
2. 🔧 Blenderで`編集 > プリファレンス > アドオン`を開く
3. ➕ `インストール...`をクリックしてダウンロードしたファイルを選択
4. ✅ "Aseprite Importer"アドオンを有効化

## 📋 必要環境

- 🟦 Blender 2.93以降（Blender 4.2以降でマニフェストサポート）
- 🎨 Asepriteがインストールされていること（デフォルトパス: `C:\Program Files\Aseprite\Aseprite.exe`）

## 🚀 使い方

1. 📂 `ファイル > インポート > Aseprite (.aseprite)`を選択
2. 🎯 `.aseprite`ファイルを選択
3. ✨ テクスチャとSolidifyモディファイアが適用されたメッシュが作成されます

## ⚙️ プリファレンス

`編集 > プリファレンス > アドオン > Aseprite Importer`からアクセス

- 📁 **Aseprite実行ファイルパス**: Asepriteのインストールパス（デフォルト: `C:\Program Files\Aseprite\Aseprite.exe`）
- 📦 **Solidifyモディファイアを追加**: インポートしたメッシュに自動的にSolidifyモディファイアを追加（デフォルト: 有効）
- 🏷️ **テクスチャプレフィックス**: エクスポートされるテクスチャファイルのプレフィックス（デフォルト: `tex_`）

## 📄 ライセンス

MITライセンス - 詳細は[LICENSE](LICENSE)を参照

## 👤 作者

kesera2
