# Frequently Asked Questions

## General

### What versions of Blender are supported?

Blender 2.93 and later. The add-on also supports Blender 4.2+ with the new manifest system.

### Do I need Aseprite installed?

Yes, the add-on uses Aseprite's command-line interface to export your `.aseprite` files to PNG format before importing into Blender.

### Can I import `.ase` files?

Yes, `.ase` is the same format as `.aseprite`. However, the file filter currently shows `.aseprite` only. You can manually select `.ase` files.

### Does this support Aseprite animations?

Currently, the add-on imports only the current frame. Animation support may be added in future versions.

## Installation & Setup

### Where can I find my Aseprite executable?

**Windows:**
- Steam: `C:\Program Files (x86)\Steam\steamapps\common\Aseprite\Aseprite.exe`
- Standalone: `C:\Program Files\Aseprite\Aseprite.exe`

**macOS:**
- `/Applications/Aseprite.app/Contents/MacOS/aseprite`

**Linux:**
- `/usr/bin/aseprite`
- `~/.steam/steam/steamapps/common/Aseprite/aseprite`

### I get "Aseprite not found" error

1. Verify Aseprite is installed
2. Check the path in `Edit > Preferences > Add-ons > Aseprite Importer`
3. Make sure the path points to the executable file (not the folder)
4. On macOS, use the path inside the `.app` bundle

### The add-on doesn't appear in the Import menu

1. Make sure you enabled the add-on (checkbox in preferences)
2. Restart Blender
3. Check the System Console (Window > Toggle System Console) for errors

## Usage

### Why is my mesh so small/large?

The mesh uses 1 Blender unit per pixel. A 32x32 pixel sprite becomes a 32x32 unit mesh. Use the Scale tool (`S` key) to adjust.

### The texture looks blurry

The add-on sets texture interpolation to "Closest" by default for pixel-perfect rendering. If it's blurry:
1. Check the Image Texture node in Shader Editor
2. Ensure Interpolation is set to "Closest"

### Can I disable the Solidify modifier?

Yes, when importing a file, uncheck "Add Solidify Modifier" in the import dialog options.

### What is the texture prefix setting for?

The add-on exports your Aseprite file as PNG with a prefix (default: `tex_`). This helps identify temporary texture files in Blender's temp directory.

### Where are the textures saved?

Textures are saved in Blender's temporary directory. They're packed with your `.blend` file if you save it. The original `.aseprite` file is not modified.

## Technical

### Does this work with Blender 4.2's new extension system?

Yes, the add-on includes `blender_manifest.toml` for Blender 4.2+ compatibility.

### Can I use this add-on commercially?

Yes, the add-on is licensed under MIT, allowing commercial use.

### How do I report a bug?

Please report bugs on the [GitHub Issues page](https://github.com/kesera2/aseprite-importer-for-blender/issues).

### Can I contribute to the project?

Yes! Pull requests are welcome. See the [GitHub repository](https://github.com/kesera2/aseprite-importer-for-blender) for contribution guidelines.

## Troubleshooting

### Import fails with no error message

1. Check Blender's System Console for detailed errors
2. Try running Aseprite manually to ensure it works
3. Verify your `.aseprite` file isn't corrupted

### "PNG export failed" error

1. Check that Aseprite has write permissions to temp directory
2. Verify the `.aseprite` file can be opened in Aseprite
3. Try a simple test file (single layer, no complex features)

### Mesh has missing faces

This is expected - transparent pixels are not converted to mesh faces. Only pixels with alpha > 0 are included.

### The UV mapping is wrong

The add-on centers UV coordinates on each pixel. If you modified the mesh after import, you may need to adjust UVs manually.
