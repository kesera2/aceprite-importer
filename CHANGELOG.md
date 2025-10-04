# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0](https://github.com/kesera2/aseprite-importer-for-blender/compare/v1.0.0...v1.1.0) (2025-10-04)


### Features

* add frame selection and auto-detection features ([7c0a8f5](https://github.com/kesera2/aseprite-importer-for-blender/commit/7c0a8f5f214d7eaa7094c78229bb66f62beb640c))

## 1.0.0 (2025-10-04)


### Features

* add custom theme, favicon, and reorganize assets ([02395d6](https://github.com/kesera2/aseprite-importer-for-blender/commit/02395d6c59be2d86be5025795a764157af477efc))
* add download button for latest release ([fe02496](https://github.com/kesera2/aseprite-importer-for-blender/commit/fe0249684c9d601721ac53d0bfe7badd956ae19b))


### Bug Fixes

* correct image path in Japanese installation guide ([f003fd3](https://github.com/kesera2/aseprite-importer-for-blender/commit/f003fd3dafac507d78b6935392fcd627080dae89))

## [Unreleased]

## [0.1.0] - 2025-10-04

### Added
- Initial release
- Import `.aseprite` files directly into Blender as 3D mesh
- Automatic conversion of pixel art to mesh geometry
- Configurable Aseprite executable path in preferences
- Optional Solidify modifier (enabled by default)
- Customizable texture prefix for exported PNG files
- Pixel-perfect UV mapping
- Transparent pixel exclusion from mesh generation
- Support for Blender 2.93+ and 4.2+ (with manifest)
- Error handling for missing Aseprite executable
- Subprocess timeout protection
- Japanese and English documentation
