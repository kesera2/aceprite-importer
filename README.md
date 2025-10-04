<div align="right">

[English](README.md) | [日本語](README.ja.md)

</div>

![Aseprite Importer](https://aseprite-importer.kesera2.dev/aseprite-importer-logo.gif)

<div align="center">

[![GitHub release](https://img.shields.io/github/v/release/kesera2/aseprite-importer-for-blender)](https://github.com/kesera2/aseprite-importer-for-blender/releases)
[![License](https://img.shields.io/github/license/kesera2/aseprite-importer-for-blender)](LICENSE)
[![Blender](https://img.shields.io/badge/Blender-2.93%2B-orange)](https://www.blender.org/)

</div>


# 🎨 Aseprite Importer for Blender

✨ Import Aseprite files as pixel mesh with solidify modifier in Blender.

📚 **[Visit Documentation Site](https://aseprite-importer.kesera2.dev)** for detailed guides and tutorials.

![Sample](docs/public/sample.png)

## ⭐ Features

- 📥 Import `.aseprite` files directly into Blender
- 🎲 Automatically converts pixel art to 3D mesh
- 📦 Applies Solidify modifier for 3D thickness
- 🖼️ Preserves pixel-perfect textures with proper UV mapping
- 🪄 Transparent pixels are excluded from mesh generation

## 💾 Installation

1. 📦 Download the latest release
2. 🔧 In Blender, go to `Edit > Preferences > Add-ons`
3. ➕ Click `Install...` and select the downloaded file
4. ✅ Enable the "Aseprite Importer" add-on

## 📋 Requirements

- 🟦 Blender 2.93 or later (Blender 4.2+ for manifest support)
- 🎨 Aseprite installed

::: tip
The add-on automatically detects Aseprite from common installation paths. Manual configuration is only needed for non-standard installations.
:::

## 🚀 Usage

1. 📂 Go to `File > Import > Aseprite (.aseprite)`
2. 🎯 Select your `.aseprite` file
3. ✨ The mesh will be created with texture and Solidify modifier applied

## ⚙️ Settings

### Preferences

Access via `Edit > Preferences > Add-ons > Aseprite Importer`:

- 📁 **Aseprite Executable Path**: Path to your Aseprite installation (default: `C:\Program Files\Aseprite\Aseprite.exe`)

### Import Options

Configure when importing a file (`File > Import > Aseprite (.aseprite)`):

- 🔢 **Frame Number**: Which frame to import from multi-frame files (default: 0)
- 📦 **Add Solidify Modifier**: Automatically add Solidify modifier (default: enabled)
- 📏 **Solidify Thickness**: Thickness of the 3D depth in meters (default: 0.1m)
- 🏷️ **Texture Prefix**: Prefix for exported texture files (default: `tex_`)

## 📄 License

MIT License - See [LICENSE](LICENSE) for details

## 👤 Author

kesera2
