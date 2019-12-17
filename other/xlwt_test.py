# -*- coding: utf-8 -*-
import xlwt
def _create_excel(data):
    workbook = xlwt.Workbook(encoding='utf-8')

    _create_basic_sheet(workbook, data)
    _create_class_sheet(workbook, data)
    _create_stat_sheet(workbook, data)

    workbook.save("aaa.xls")

    return workbook

def _create_basic_sheet(workbook, data):
    basic_info_sheet = workbook.add_sheet("基本信息",cell_overwrite_ok=True)
    basic_rows = [
        ['课程名称',''],
        ['开课学院',''],
        ['课程负责人',''],
        ['单期课程开设周数',''],
    ]

    for i in range(len(basic_rows)):
        for j in range(len(basic_rows[i])):
            basic_info_sheet.write(i,j,basic_rows[i][j])

def _create_class_sheet(workbook, data):
    class_info_sheet = workbook.add_sheet("课程开课情况",cell_overwrite_ok=True)
    class_rows = [
        ['序号','起止时间','社会学习者选课人数','课程链接','高校选课人数','课程链接','选课总人数',]
    ]

    for i in range(len(class_rows)):
        for j in range(len(class_rows[i])):
            class_info_sheet.write(i,j,class_rows[i][j])

def _create_stat_sheet(workbook, data):
    sheet = workbook.add_sheet("课程资源与学习数据",cell_overwrite_ok=True)
    rows = [
        ['数据项','','第()学期','第()学期'],
        ['授课视频','总数量（个）','',''],
        ['','总时长（分钟）','',''],
        ['非视频资源','数量（个） ','',''],
        ['课程公告','数量(次)','',''],
        ['测验和作业','总次数（次）','',''],
        ['','习题总数（道）','',''],
        ['','参与人数（人）','',''],
        ['互动交流情况','发帖总数(贴)','',''],
        ['','教师发帖数(贴）','',''],
        ['','参与互动人数（人）','',''],
        ['考核(试)','次数(次）','',''],
        ['','试题总数（题）','',''],
        ['','参与人数（人）','',''],
        ['','课程通过人数（人）','',''],
        ['学校使用情况','使用课程学校总数','',''],
        ['','使用课程学校名称','',''],
        ['','选课总人数','',''],
        ['课程备注','','',''],
    ]

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            sheet.write(i,j,rows[i][j])

    alignment = xlwt.Alignment()
    style = xlwt.XFStyle()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style.alignment = alignment

    sheet.write_merge(0,0,0,1,"数据项",style)
    sheet.write_merge(1,2,0,0,"授课视频",style)
    sheet.write_merge(5,7,0,0,"测验和作业",style)
    sheet.write_merge(8,10,0,0,"互动交流情况",style)
    sheet.write_merge(11,14,0,0,"考核(试)",style)
    sheet.write_merge(15,17,0,0,"学校使用情况",style)
    sheet.write_merge(18,18,1,3,"",style)

    sheet.col(1).width = 256 * 20


_create_excel([])