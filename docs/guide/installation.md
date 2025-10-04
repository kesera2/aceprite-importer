# Installation Guide

## Prerequisites

- Blender 2.93 or later
- Aseprite installed on your system

## Installation Steps

### 1. Download the Add-on

Download the latest `aseprite-importer.zip` from the [Releases page](https://github.com/kesera2/aseprite-importer-for-blender/releases).

### 2. Install in Blender

1. Open Blender
2. Go to `Edit > Preferences` (or `Blender > Preferences` on macOS)
3. Select the `Add-ons` tab
4. Click the `Install...` button at the top right
5. Navigate to the downloaded `aseprite-importer.zip` file
6. Click `Install Add-on`
7. Enable the add-on by checking the checkbox next to "Import-Export: Aseprite Importer"

### 3. Configure Aseprite Path

1. In the Add-ons preferences, expand "Aseprite Importer"
2. Set the **Aseprite Executable Path** to your Aseprite installation:
   - Windows: `C:\Program Files\Aseprite\Aseprite.exe` (default)
   - macOS: `/Applications/Aseprite.app/Contents/MacOS/aseprite`
   - Linux: `/usr/bin/aseprite` or `~/.steam/steam/steamapps/common/Aseprite/aseprite`

![Preferences](/aseprite-importer-for-blender-preference.png)

### 4. Optional Settings

- **Add Solidify Modifier**: Enable/disable automatic Solidify modifier (default: enabled)
- **Texture Prefix**: Set prefix for exported texture files (default: `tex_`)

## Verification

To verify the installation:
1. Go to `File > Import`
2. You should see "Aseprite (.aseprite)" in the import menu

## Troubleshooting

### "Aseprite not found" Error

If you get this error:
1. Check that Aseprite is installed
2. Verify the path in Add-on preferences is correct
3. On macOS/Linux, ensure the executable has proper permissions

### Add-on Not Appearing

1. Make sure you enabled the add-on (checkbox)
2. Try restarting Blender
3. Check Blender's console for error messages
