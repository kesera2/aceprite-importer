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

The add-on will automatically detect your Aseprite installation on first use. To verify or change the path:

1. In the Add-ons preferences, expand "Aseprite Importer"
2. Check the **Status** indicator:
   - ✓ **Aseprite executable found**: The path is correctly configured
   - ✗ **Aseprite executable not found**: You need to set the correct path

3. If needed, manually set the **Aseprite Executable Path**:
   - Windows: `C:\Program Files\Aseprite\Aseprite.exe` (default) or `C:\Program Files (x86)\Steam\steamapps\common\Aseprite\Aseprite.exe` (Steam)
   - macOS: `/Applications/Aseprite.app/Contents/MacOS/aseprite`
   - Linux: `/usr/bin/aseprite` or `~/.steam/steam/steamapps/common/Aseprite/aseprite` (Steam)

![Preferences](/aseprite-importer-for-blender-preference.png)

::: tip Auto-Detection
The add-on automatically searches common installation locations. If Aseprite is installed in a non-standard location, you'll need to set the path manually.
:::

## Verification

To verify the installation:
1. Go to `File > Import`
2. You should see "Aseprite (.aseprite)" in the import menu

## Troubleshooting

### "Aseprite not found" Error

If you get this error:
1. Check the **Status** indicator in Add-on preferences
2. If the status shows "not found", verify that Aseprite is installed
3. Check the expected locations listed in the preferences panel
4. On macOS/Linux, ensure the executable has proper permissions

### Add-on Not Appearing

1. Make sure you enabled the add-on (checkbox)
2. Try restarting Blender
3. Check Blender's console for error messages
