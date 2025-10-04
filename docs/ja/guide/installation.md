# インストールガイド

## 前提条件

- Blender 2.93以降
- Asepriteがインストールされていること

## インストール手順

### 1. アドオンのダウンロード

[リリースページ](https://github.com/kesera2/aceprite-importer/releases)から最新の`aseprite-importer.zip`をダウンロードします。

### 2. Blenderにインストール

1. Blenderを開く
2. `編集 > プリファレンス`（macOSでは`Blender > プリファレンス`）を開く
3. `アドオン`タブを選択
4. 右上の`インストール...`ボタンをクリック
5. ダウンロードした`aseprite-importer.zip`ファイルを選択
6. `アドオンをインストール`をクリック
7. "Import-Export: Aseprite Importer"の横のチェックボックスをオンにしてアドオンを有効化

### 3. Asepriteパスの設定

1. アドオンのプリファレンスで"Aseprite Importer"を展開
2. **Aseprite実行ファイルパス**をAsepriteのインストール先に設定：
   - Windows: `C:\Program Files\Aseprite\Aseprite.exe`（デフォルト）
   - macOS: `/Applications/Aseprite.app/Contents/MacOS/aseprite`
   - Linux: `/usr/bin/aseprite` または `~/.steam/steam/steamapps/common/Aseprite/aseprite`

![プリファレンス](/aseprite-importer-for-blender-preference.png)

### 4. オプション設定

- **Solidifyモディファイアを追加**: 自動Solidifyモディファイアの有効/無効（デフォルト: 有効）
- **テクスチャプレフィックス**: エクスポートされるテクスチャファイルのプレフィックス設定（デフォルト: `tex_`）

## 動作確認

インストールを確認するには：
1. `ファイル > インポート`を開く
2. インポートメニューに"Aseprite (.aseprite)"が表示されるはずです

## トラブルシューティング

### "Aseprite not found"エラー

このエラーが出た場合：
1. Asepriteがインストールされているか確認
2. アドオンのプリファレンスでパスが正しいか確認
3. macOS/Linuxでは実行ファイルに適切な権限があるか確認

### アドオンが表示されない

1. アドオンを有効化（チェックボックス）したか確認
2. Blenderを再起動してみる
3. Blenderのコンソールでエラーメッセージを確認
