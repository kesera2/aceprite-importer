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

アドオンは初回使用時にAsepriteのインストール先を自動的に検出します。パスを確認または変更するには：

1. アドオンのプリファレンスで"Aseprite Importer"を展開
2. **ステータス**インジケーターを確認：
   - ✓ **Aseprite実行ファイルが見つかりました**: パスが正しく設定されています
   - ✗ **Aseprite実行ファイルが見つかりません**: 正しいパスを設定する必要があります

3. 必要に応じて、**Aseprite実行ファイルパス**を手動で設定：
   - Windows: `C:\Program Files\Aseprite\Aseprite.exe`（デフォルト）または `C:\Program Files (x86)\Steam\steamapps\common\Aseprite\Aseprite.exe`（Steam版）
   - macOS: `/Applications/Aseprite.app/Contents/MacOS/aseprite`
   - Linux: `/usr/bin/aseprite` または `~/.steam/steam/steamapps/common/Aseprite/aseprite`（Steam版）

![プリファレンス](/aseprite-importer-for-blender-preference-ja.png)

::: tip 自動検出
アドオンは一般的なインストール場所を自動的に検索します。Asepriteが標準的でない場所にインストールされている場合は、手動でパスを設定してください。
:::

## 動作確認

インストールを確認するには：
1. `ファイル > インポート`を開く
2. インポートメニューに"Aseprite (.aseprite)"が表示されるはずです

## トラブルシューティング

### "Aseprite not found"エラー

このエラーが出た場合：
1. アドオンのプリファレンスで**ステータス**インジケーターを確認
2. ステータスが「見つかりません」の場合、Asepriteがインストールされているか確認
3. プリファレンスパネルに表示される予想される場所を確認
4. macOS/Linuxでは実行ファイルに適切な権限があるか確認

### アドオンが表示されない

1. アドオンを有効化（チェックボックス）したか確認
2. Blenderを再起動してみる
3. Blenderのコンソールでエラーメッセージを確認
