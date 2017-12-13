# coding: utf-8
import math
import csv
from datetime import datetime

import arcpy

# FC 表示 Feature Class
corePointFC = 'C:/Users/Mookrs/Desktop/EddyGDB.gdb/CorePoint'
processFC = 'C:/Users/Mookrs/Desktop/EddyGDB.gdb/Process'

coreIDField = 'CoreID'
corePointFields = ['CoreID', 'X', 'Y', 'Time', 'NextCoreID']
processFields = ['StartCoreID', 'EndCoreID']

# 按 Process 分好组的 Point 集合
pointsInProcesses = []


# 定义类


class Coord:
    """ 坐标：包含x、y """
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)


class Point:
    """ 点: 包含坐标、时间"""
    coord = Coord(0, 0)
    time = ''

    def __init__(self, coord, time):
        self.coord = coord
        self.time = time

    def __str__(self):
        return 'Coord: {0}, Time: {1}'.format(self.coord, self.time)


class StayPoint:
    """ 停留点：包含x、y、到达时间、离开时间 """
    x = 0
    y = 0
    arvT = ''
    levT = ''

    def __init__(self):
        pass

    def __str__(self):
        return 'Coord: ({0}, {1}), Arrival time: {2}, Leaving time: {3}'.format(
            self.x, self.y, self.arvT, self.levT)


# 定义函数


def StayPointDetection(points, distThreh, timeThreh):
    """ 判断停留点 """
    i = 0
    pointNum = len(points)
    stayPoints = []
    while i < pointNum:
        j = i + 1
        token = 0
        while j < pointNum:
            dist = Distance(points[i], points[j])
            if dist > distThreh:
                timespan = ComputTimespan(points[j].time, points[i].time)
                if timespan > timeThreh:
                    s = StayPoint()
                    coord = ComputMeanCoord(points[i], points[j])
                    s.x, s.y = coord.x, coord.y
                    s.arvT = points[i].time
                    s.levT = points[j].time
                    stayPoints.append(s)

                    i = j
                    token = 1
                break
            j += 1

        if token != 1:
            i += 1

    return stayPoints


def StrToDate(date_str):
    """ 将 YYYYMMDD 格式的字符串转换为 datetime 对象 """
    return datetime.strptime(date_str, '%Y%m%d')


def ComputTimespan(dt1, dt2):
    """ 返回两个时间字符串的天数差 """
    return (StrToDate(dt1) - StrToDate(dt2)).days


def Distance(p1, p2):
    """ 计算两点距离 """
    dist = math.sqrt((p1.coord.x - p2.coord.x) ** 2 + (p1.coord.y - p2.coord.y) ** 2)
    return dist


def ComputMeanCoord(p1, p2):
    """ 计算两点中间坐标 """
    x = (p1.coord.x + p2.coord.x) / 2.0
    y = (p1.coord.y + p2.coord.y) / 2.0
    return Coord(x, y)


# 执行部分


if __name__ == '__main__':
    # 打开 gdb 文件的 Process 层
    with arcpy.da.SearchCursor(processFC, processFields) as cursor:
        # 遍历 Process 中的行
        for row in cursor:
            startCoreID = row[0]
            endCoreID = row[1]
            pointsInOneProcess = []
            # 在 CorePoint 层中寻找 CoreID 等于 Process 层中某一行 StartCoreID 的记录
            expression = arcpy.AddFieldDelimiters(corePointFC, coreIDField) + " = '" + startCoreID + "'"

            with arcpy.da.SearchCursor(corePointFC, corePointFields, where_clause=expression) as cursor2:
                # 遍历查找到的 CorePoint 层中的行，理论上来说只有一个结果
                for row2 in cursor2:
                    # 起始点
                    firstPoint = Point(Coord(row2[1], row2[2]), row2[3])
                    pointsInOneProcess.append(firstPoint)

                    currentCoreID = row2[0]
                    nextCoreID = row2[4]
                    while nextCoreID != 'End':
                        # 在 CorePoint 层中寻找 CoreID 等于上一条记录 nextCoreID 的记录
                        expression2 = arcpy.AddFieldDelimiters(corePointFC, coreIDField) + " = '" + nextCoreID + "'"

                        with arcpy.da.SearchCursor(corePointFC, corePointFields, where_clause=expression2) as cursor3:
                            # (同cursor2) 遍历查找到的 CorePoint 层中的行，理论上来说只有一个结果
                            for row3 in cursor3:
                                p = Point(Coord(row3[1], row3[2]), row3[3])
                                pointsInOneProcess.append(p)

                                currentCoreID = row3[0]
                                nextCoreID = row3[4]

                    if currentCoreID == endCoreID:
                        print 'Added pointsInOneProcess. First point is: ' + str(pointsInOneProcess[0])
                        pointsInProcesses.append(pointsInOneProcess)

    print 'Grouping pointsInProcesses has finished!'

    # 包判别结果保存到 csv 文件中
    with open('StayPoints.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for pnts in pointsInProcesses:
            # 判别停留点，返回停留点集合
            sps = StayPointDetection(pnts, 999, -1)
            # 不为空
            if sps:
                # TODO 考虑如何为停留点分组
                writer.writerow([-1])
                for sp in sps:
                    writer.writerow([sp.x, sp.y, sp.arvT, sp.levT])
