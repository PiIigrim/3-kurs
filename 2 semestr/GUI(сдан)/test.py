import bpy
import bmesh

# собсна создание треугольников
def triangulate_quad(face, bm):
    verts = [v for v in face.verts]
    v0, v1, v2, v3 = verts
    bm.faces.remove(face)
    bm.faces.new([v0, v1, v2])
    bm.faces.new([v0, v2, v3])

def divide_and_conquer_tri(obj):
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)

    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.subdivide(number_cuts=1)

    # проходимся по каждому "лицу" и делаем треугольники
    for face in bm.faces[:]:
        if len(face.verts) == 4:  # работает только с 4-угольниками
            triangulate_quad(face, bm)

    bpy.ops.object.mode_set(mode='OBJECT')
    bm.to_mesh(mesh)
    bm.free()

# прозодимся по каждому обьекту(если он есть)
def divide_and_conquer_recursive(obj):
    if obj.type == 'MESH':
        divide_and_conquer_tri(obj)

    for child in obj.children:
        divide_and_conquer_recursive(child)

selected_obj = bpy.context.active_object

if selected_obj and selected_obj.type == 'MESH':
    divide_and_conquer_recursive(selected_obj)
else:
    print("Выбранный объект не является мешем.")
