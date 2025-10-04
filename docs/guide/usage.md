# Usage Guide

## Basic Usage

### Importing an Aseprite File

1. Open Blender
2. Go to `File > Import > Aseprite (.aseprite)`
3. Navigate to your `.aseprite` file
4. Click `Import Aseprite as Mesh`
5. The mesh will be created at the world origin with texture applied

### What Gets Created

When you import an Aseprite file, the add-on automatically:

- **Converts pixels to 3D mesh**: Each non-transparent pixel becomes a quad face
- **Applies UV mapping**: Pixel-perfect UV coordinates centered on each pixel
- **Creates material**: Principled BSDF with the texture set to "Closest" interpolation
- **Adds Solidify modifier** (if enabled): Gives 3D thickness to the flat mesh
- **Sets alpha blending**: Material uses "Clip" blend mode for transparency

## Understanding the Result

### Mesh Structure

- Each visible pixel becomes a 1x1 unit quad
- Transparent pixels are excluded
- Duplicate vertices are merged automatically
- Origin is set to center of mass

### Solidify Modifier

If enabled in preferences, the Solidify modifier:
- **Thickness**: 0.1 units (adjustable in modifier panel)
- **Offset**: 1.0 (extrudes outward)
- **Rim**: Enabled (creates side faces)

You can modify these settings after import in the Modifiers panel.

### Texture

The texture is temporarily exported as PNG in Blender's temp directory with the prefix specified in preferences (default: `tex_`).

## Tips and Tricks

### Scaling

The imported mesh uses 1 Blender unit per pixel. To scale:
1. Select the object
2. Press `S` to scale
3. Enter desired scale factor

### Editing the Mesh

After import, you can:
- Modify the Solidify thickness in the Modifiers panel
- Edit UVs if needed
- Add additional modifiers
- Edit the mesh in Edit mode

### Texture Interpolation

The texture uses "Closest" interpolation by default to maintain pixel-perfect appearance. To change:
1. Go to Shader Editor
2. Select the Image Texture node
3. Change Interpolation setting

### Re-importing

If you update your Aseprite file:
1. Simply re-import the file
2. A new object will be created
3. Delete the old object if needed

## Common Workflows

### Game Asset Creation

1. Import Aseprite sprite
2. Adjust Solidify thickness for desired depth
3. Add Array modifier for patterns
4. Export as FBX/GLTF for game engine

### Animation Setup

1. Import multiple frames as separate files
2. Use as keyframes for stop-motion style animation
3. Or use Aseprite's layer export and import each as separate object

### Rendering

1. Set up lighting for pixel art (avoid soft shadows)
2. Use Eevee or Cycles
3. Disable anti-aliasing for crisp pixel edges
4. Render at multiples of native resolution (2x, 3x, 4x)
