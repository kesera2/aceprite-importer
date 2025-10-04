bl_info = {
    "name": "Aseprite Importer",
    "author": "kesera2",
    "version": (1, 1, 0),
    "blender": (2, 93, 0),
    "location": "File > Import > Aseprite (.aseprite)",
    "description": "Import an Aseprite file as pixel mesh with solidify modifier",
    "category": "Import-Export",
}

import bpy
import os
import subprocess
import sys
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty
import bmesh

def find_aseprite_path():
    """Find Aseprite executable path based on OS"""
    possible_paths = []

    if sys.platform == "win32":
        # Windows
        possible_paths = [
            r"C:\Program Files\Aseprite\Aseprite.exe",
            r"C:\Program Files (x86)\Steam\steamapps\common\Aseprite\Aseprite.exe",
            os.path.expanduser(r"~\AppData\Local\Aseprite\Aseprite.exe"),
        ]
    elif sys.platform == "darwin":
        # macOS
        possible_paths = [
            "/Applications/Aseprite.app/Contents/MacOS/aseprite",
            os.path.expanduser("~/Applications/Aseprite.app/Contents/MacOS/aseprite"),
        ]
    else:
        # Linux
        possible_paths = [
            "/usr/bin/aseprite",
            "/usr/local/bin/aseprite",
            os.path.expanduser("~/.steam/steam/steamapps/common/Aseprite/aseprite"),
            os.path.expanduser("~/.local/share/Steam/steamapps/common/Aseprite/aseprite"),
        ]

    # Return first existing path, or default Windows path
    for path in possible_paths:
        if os.path.exists(path):
            return path

    # Default fallback
    return r"C:\Program Files\Aseprite\Aseprite.exe" if sys.platform == "win32" else "/usr/bin/aseprite"

# Translation dictionary
translation_dict = {
    "ja_JP": {
        ("*", "Aseprite Executable Path"): "Aseprite実行ファイルパス",
        ("*", "Path to Aseprite executable"): "Asepriteの実行ファイルのパス",
        ("*", "Aseprite Settings:"): "Aseprite設定:",
        ("*", "Import Options:"): "インポートオプション:",
        ("*", "Status: Aseprite executable found"): "ステータス: Aseprite実行ファイルが見つかりました",
        ("*", "Status: Aseprite executable not found"): "ステータス: Aseprite実行ファイルが見つかりません",
        ("*", "Expected locations:"): "予想される場所:",
        ("*", "Frame Number"): "フレーム番号",
        ("*", "Frame number to import from the Aseprite file (0 = first frame, 1 = second frame, etc.)"): "Asepriteファイルからインポートするフレーム番号（0 = 最初のフレーム、1 = 2番目のフレーム、など）",
        ("*", "Add Solidify Modifier"): "Solidifyモディファイアを追加",
        ("*", "Automatically add Solidify modifier to give 3D thickness to the imported pixel mesh"): "インポートしたピクセルメッシュに3Dの厚みを与えるためにSolidifyモディファイアを自動的に追加",
        ("*", "Solidify Thickness"): "Solidifyの幅",
        ("*", "Thickness of the Solidify modifier in meters (only used when Add Solidify Modifier is enabled)"): "Solidifyモディファイアの幅（メートル単位、Solidifyモディファイアを追加が有効な場合のみ使用）",
        ("*", "Texture Prefix"): "テクスチャプレフィックス",
        ("*", "Prefix added to exported texture files (e.g., 'tex_' creates 'tex_sprite.png')"): "エクスポートされるテクスチャファイルに追加されるプレフィックス（例: 'tex_'で'tex_sprite.png'が作成されます）",
    }
}

class AsepriteImporterPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    aseprite_path: StringProperty(
        name="Aseprite Executable Path",
        description="Path to Aseprite executable",
        default="",
        subtype='FILE_PATH',
        maxlen=1024
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Aseprite Settings:")
        layout.prop(self, "aseprite_path")

        # Show status of Aseprite path
        if self.aseprite_path and os.path.exists(self.aseprite_path):
            row = layout.row()
            row.label(text="Status: Aseprite executable found", icon='CHECKMARK')
        else:
            row = layout.row()
            row.label(text="Status: Aseprite executable not found", icon='ERROR')
            box = layout.box()
            box.label(text="Expected locations:", icon='INFO')
            if sys.platform == "win32":
                box.label(text="  C:\\Program Files\\Aseprite\\Aseprite.exe")
                box.label(text="  C:\\Program Files (x86)\\Steam\\steamapps\\common\\Aseprite\\Aseprite.exe")
            elif sys.platform == "darwin":
                box.label(text="  /Applications/Aseprite.app/Contents/MacOS/aseprite")
            else:
                box.label(text="  /usr/bin/aseprite")
                box.label(text="  ~/.steam/steam/steamapps/common/Aseprite/aseprite")

class ImportAseprite(bpy.types.Operator, ImportHelper):
    """Import an Aseprite file and convert to mesh"""
    bl_idname = "import_scene.aseprite_mesh"
    bl_label = "Import Aseprite as Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    filename_ext = ".aseprite"
    filter_glob: StringProperty(
        default="*.aseprite",
        options={'HIDDEN'},
        maxlen=255,
    )

    frame_number: bpy.props.IntProperty(
        name="Frame Number",
        description="Frame number to import from the Aseprite file (0 = first frame, 1 = second frame, etc.)",
        default=0,
        min=0,
    )

    add_solidify: BoolProperty(
        name="Add Solidify Modifier",
        description="Automatically add Solidify modifier to give 3D thickness to the imported pixel mesh",
        default=True
    )

    solidify_thickness: bpy.props.FloatProperty(
        name="Solidify Thickness",
        description="Thickness of the Solidify modifier in meters (only used when Add Solidify Modifier is enabled)",
        default=0.1,
        min=-10.0,
        max=10.0,
        unit='LENGTH',
        subtype='DISTANCE',
    )

    texture_prefix: StringProperty(
        name="Texture Prefix",
        description="Prefix added to exported texture files (e.g., 'tex_' creates 'tex_sprite.png')",
        default="tex_",
        maxlen=64
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Import Options:")
        layout.prop(self, "frame_number")
        layout.prop(self, "add_solidify")
        if self.add_solidify:
            layout.prop(self, "solidify_thickness")
        layout.prop(self, "texture_prefix")

    def execute(self, context):
        # プリファレンスからAsepriteのパスを取得
        preferences = context.preferences.addons[__name__].preferences
        aseprite_path = preferences.aseprite_path

        # Asepriteの実行ファイルが存在するか確認
        if not os.path.exists(aseprite_path):
            self.report({'ERROR'}, f"Aseprite not found at: {aseprite_path}. Please set the correct path in Preferences > Add-ons > Aseprite Importer")
            return {'CANCELLED'}

        # 1. AsepriteファイルをPNGに変換
        aseprite_file = os.path.abspath(self.filepath)
        file_name = os.path.splitext(os.path.basename(aseprite_file))[0]
        tmp_dir = bpy.app.tempdir
        png_path = os.path.join(tmp_dir, f"{self.texture_prefix}{file_name}.png")

        # 既存のPNGファイルがあれば削除
        if os.path.exists(png_path):
            os.remove(png_path)

        # 指定されたフレームをエクスポート
        frame_range = f"{self.frame_number},{self.frame_number}"
        result = subprocess.run(
            [aseprite_path, "-b", aseprite_file, "--frame-range", frame_range, "--save-as", png_path],
            capture_output=True, text=True
        )

        if result.returncode != 0 or not os.path.exists(png_path):
            error_msg = result.stderr if result.stderr else result.stdout if result.stdout else "Unknown error"
            self.report({'ERROR'}, f"PNG export failed (return code: {result.returncode}): {error_msg}")
            return {'CANCELLED'}

        # 画像を読み込む
        image = bpy.data.images.load(png_path)
        w, h = image.size[0], image.size[1]
        pixels = list(image.pixels)

        # 2. ドットごとにメッシュを生成
        mesh = bpy.data.meshes.new(file_name)
        bm = bmesh.new()

        uv_layer = bm.loops.layers.uv.new()

        for y in range(h):
            for x in range(w):
                idx = (y * w + x) * 4
                r, g, b, a = pixels[idx:idx+4]

                if a > 0.0:  # アルファが0より大きいピクセルのみ
                    # 4つの頂点を作成
                    v1 = bm.verts.new((x, y, 0))
                    v2 = bm.verts.new((x + 1, y, 0))
                    v3 = bm.verts.new((x + 1, y + 1, 0))
                    v4 = bm.verts.new((x, y + 1, 0))

                    # 面を作成
                    face = bm.faces.new((v1, v2, v3, v4))

                    # 3. UV座標を設定（ピクセル中心に合わせる）
                    half_pixel_u = 0.5 / w
                    half_pixel_v = 0.5 / h
                    face.loops[0][uv_layer].uv = ((x + 0.5) / w, (y + 0.5) / h)
                    face.loops[1][uv_layer].uv = ((x + 0.5) / w, (y + 0.5) / h)
                    face.loops[2][uv_layer].uv = ((x + 0.5) / w, (y + 0.5) / h)
                    face.loops[3][uv_layer].uv = ((x + 0.5) / w, (y + 0.5) / h)

        # 重複頂点を結合
        bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.0001)

        bm.to_mesh(mesh)
        bm.free()

        # オブジェクトを作成
        obj = bpy.data.objects.new(file_name, mesh)
        context.collection.objects.link(obj)
        context.view_layer.objects.active = obj
        obj.select_set(True)

        # マテリアルを設定
        mat = bpy.data.materials.new(name=file_name)
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links

        nodes.clear()
        bsdf = nodes.new('ShaderNodeBsdfPrincipled')
        tex = nodes.new('ShaderNodeTexImage')
        output = nodes.new('ShaderNodeOutputMaterial')

        tex.image = image
        tex.interpolation = 'Closest'

        links.new(tex.outputs['Color'], bsdf.inputs['Base Color'])
        links.new(tex.outputs['Alpha'], bsdf.inputs['Alpha'])
        links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])

        mat.blend_method = 'CLIP'
        obj.data.materials.append(mat)

        # 4. メッシュの原点を重心に変更し、ワールド原点に移動
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='MEDIAN')
        obj.location = (0, 0, 0)

        # Solidifyモディファイアを追加（オプションで有効な場合のみ）
        if self.add_solidify:
            solid = obj.modifiers.new("Solidify", 'SOLIDIFY')
            solid.thickness = self.solidify_thickness
            solid.offset = 1.0  # 外側に厚みを出す（-1.0で内側）
            solid.use_rim = True  # 側面を生成
            solid.use_rim_only = False

        return {'FINISHED'}

def menu_func_import(self, context):
    self.layout.operator(ImportAseprite.bl_idname, text="Aseprite (.aseprite)")

def register():
    # 既存のクラスを削除
    try:
        bpy.utils.unregister_class(AsepriteImporterPreferences)
    except Exception as e:
        print(f"Warning: Could not unregister AsepriteImporterPreferences: {e}")
    try:
        bpy.utils.unregister_class(ImportAseprite)
    except Exception as e:
        print(f"Warning: Could not unregister ImportAseprite: {e}")

    # すべての同名の関数を削除
    for func in list(bpy.types.TOPBAR_MT_file_import._dyn_ui_initialize()):
        if hasattr(func, '__name__') and func.__name__ == 'menu_func_import':
            try:
                bpy.types.TOPBAR_MT_file_import.remove(func)
            except Exception as e:
                print(f"Warning: Could not remove menu_func_import: {e}")

    bpy.utils.register_class(AsepriteImporterPreferences)
    bpy.utils.register_class(ImportAseprite)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

    # Set default Aseprite path if not already set or if current path doesn't exist
    preferences = bpy.context.preferences.addons[__name__].preferences
    if not preferences.aseprite_path or not os.path.exists(preferences.aseprite_path):
        detected_path = find_aseprite_path()
        preferences.aseprite_path = detected_path

        # Check if the detected path actually exists
        if os.path.exists(detected_path):
            print(f"Aseprite Importer: Aseprite found at {detected_path}")
        else:
            print(f"Aseprite Importer: WARNING - Aseprite executable not found!")
            print(f"Aseprite Importer: Please set the correct path in Edit > Preferences > Add-ons > Aseprite Importer")
            print(f"Aseprite Importer: Expected locations:")
            if sys.platform == "win32":
                print(f"  - C:\\Program Files\\Aseprite\\Aseprite.exe")
                print(f"  - C:\\Program Files (x86)\\Steam\\steamapps\\common\\Aseprite\\Aseprite.exe")
            elif sys.platform == "darwin":
                print(f"  - /Applications/Aseprite.app/Contents/MacOS/aseprite")
            else:
                print(f"  - /usr/bin/aseprite")
                print(f"  - ~/.steam/steam/steamapps/common/Aseprite/aseprite")

    # Register translations
    bpy.app.translations.register(__name__, translation_dict)

def unregister():
    # Unregister translations
    bpy.app.translations.unregister(__name__)

    try:
        bpy.utils.unregister_class(ImportAseprite)
    except Exception as e:
        print(f"Warning: Could not unregister ImportAseprite: {e}")
    try:
        bpy.utils.unregister_class(AsepriteImporterPreferences)
    except Exception as e:
        print(f"Warning: Could not unregister AsepriteImporterPreferences: {e}")
    try:
        bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    except Exception as e:
        print(f"Warning: Could not remove menu_func_import: {e}")

if __name__ == "__main__":
    register()
