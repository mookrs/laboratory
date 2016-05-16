# coding: utf-8
"""
    地理坐标转换成需要的投影坐标。
    放到年份文件夹下执行（如 1993，和 19931 等文件夹同级），将更改文件夹中全部文件的投影为 Robinson，
    并在 1993 同级目录生成 1993_project 文件夹，用于存放更改了投影的 raster 文件。
"""

import arcpy, os

def project_raster(in_dataset, out_dataset):
    try:
        coord_sys = arcpy.SpatialReference(54030)
        arcpy.ProjectRaster_management(in_dataset, out_dataset, coord_sys, 'NEAREST', '#', '#', '#', '#')
    
    except:
        print 'Error location: ' + in_dataset
        print arcpy.GetMessages()


current_dir_path = os.path.dirname(os.path.abspath(__file__))   # 脚本所在目录 例：1993
project_dir_path = current_dir_path + '_project'    # 创建所需的投影目录 例：1993_project
if not os.path.exists(project_dir_path):
    os.mkdir(project_dir_path)

arcpy.env.workspace = current_dir_path
dir_paths = [d for d in os.listdir('.') if os.path.isdir(d) and d != 'info']

for dir_path in dir_paths:
    out_dataset = os.path.join(project_dir_path, dir_path)
    project_raster(dir_path, out_dataset)