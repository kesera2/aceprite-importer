![Aseprite Importer](aseprite-importer-logo.gif)

<div align="right">

[English](README.md) | [日本語](README.ja.md)

</div>

# 🎨 Aseprite Importer

✨ Import Aseprite files as pixel mesh with solidify modifier in Blender.

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
- 🎨 Aseprite installed (default path: `C:\Program Files\Aseprite\Aseprite.exe`)

## 🚀 Usage

1. 📂 Go to `File > Import > Aseprite (.aseprite)`
2. 🎯 Select your `.aseprite` file
3. ✨ The mesh will be created with texture and Solidify modifier applied

## ⚙️ Preferences

Access preferences via `Edit > Preferences > Add-ons > Aseprite Importer`

- 📁 **Aseprite Executable Path**: Path to your Aseprite installation (default: `C:\Program Files\Aseprite\Aseprite.exe`)
- 📦 **Add Solidify Modifier**: Automatically add Solidify modifier to imported meshes (default: enabled)
- 🏷️ **Texture Prefix**: Prefix for exported texture files (default: `tex_`)

## 📄 License

MIT License - See [LICENSE](LICENSE) for details

## 👤 Author

kesera2
