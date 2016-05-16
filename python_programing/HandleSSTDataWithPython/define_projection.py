# coding: utf-8
"""
    添加地理坐标。
    放到 `ascii_to_raster` 脚本生成的 raster 文件夹下执行，将更改该目录下所有 raster 文件的投影。
"""

import arcpy, os, re

def define_projection(in_dataset):
    try:
        coord_sys = arcpy.SpatialReference(4326)
        arcpy.DefineProjection_management(in_dataset, coord_sys)
    
        # print arcpy.GetMessages(0)
        
    except arcpy.ExecuteError:
        print 'Error location: ' + in_dataset
        print arcpy.GetMessages(2)
        
    except Exception as ex:
        print ex.args[0]


current_dir = os.path.dirname(os.path.abspath(__file__))
arcpy.env.workspace = current_dir

for root, dirs, files in os.walk(os.path.abspath('.')):
    if re.match( r'(.*)\\\d{4}$', root):
        for subdir in dirs:
            if subdir != 'info':
                define_projection(os.path.join(root, subdir))
        print '*************** Finished %s **************' % root