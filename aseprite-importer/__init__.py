bl_info = {
    "name": "Aseprite Importer",
    "author": "kesera2",
    "version": (1, 0, 0),
    "blender": (2, 93, 0),
    "location": "File > Import > Aseprite (.aseprite)",
    "description": "Import an Aseprite file as pixel mesh with solidify modifier",
    "category": "Import-Export",
}

import bpy
import os
import subprocess
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty
import bmesh

class AsepriteImporterPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    aseprite_path: StringProperty(
        name="Aseprite Executable Path",
        description="Path to Aseprite executable",
        default=r"C:\Program Files\Aseprite\Aseprite.exe",
        subtype='FILE_PATH',
        maxlen=1024
    )

    add_solidify: BoolProperty(
        name="Add Solidify Modifier",
        description="Automatically add Solidify modifier to imported meshes",
        default=True
    )

    texture_prefix: StringProperty(
        name="Texture Prefix",
        description="Prefix for exported texture files",
        default="tex_",
        maxlen=64
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Aseprite Settings:")
        layout.prop(self, "aseprite_path")
        layout.prop(self, "add_solidify")
        layout.prop(self, "texture_prefix")

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

    def execute(self, context):
        # プリファレンスからAsepriteのパスを取得
        preferences = context.preferences.addons[__name__].preferences
        aseprite_path = preferences.aseprite_path

        # 1. AsepriteファイルをPNGに変換
        aseprite_file = os.path.abspath(self.filepath)
        file_name = os.path.splitext(os.path.basename(aseprite_file))[0]
        tmp_dir = bpy.app.tempdir
        png_path = os.path.join(tmp_dir, f"{preferences.texture_prefix}{file_name}.png")

        result = subprocess.run(
            [aseprite_path, "-b", aseprite_file, "--save-as", png_path],
            capture_output=True, text=True
        )

        if not os.path.exists(png_path):
            self.report({'ERROR'}, f"PNG export failed: {result.stderr}")
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

        # Solidifyモディファイアを追加（プリファレンスで有効な場合のみ）
        if preferences.add_solidify:
            solid = obj.modifiers.new("Solidify", 'SOLIDIFY')
            solid.thickness = 0.1
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

def unregister():
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
