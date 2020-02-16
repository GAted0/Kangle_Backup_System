import os
import shutil
import zipfile
import datetime
from os.path import join, getsize

# 设置你的FTP更目录
STATIC_DIR = '/kangle/'

now = datetime.datetime.now()


def unzip(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('这不是zip格式的文件')


def unzip_file(node_name):
    day_dir_name = str(now.strftime('%Y%m%d')) + 'f'
    unzip_dir = os.path.join(STATIC_DIR, node_name, day_dir_name)
    zip_file_name = str(now.strftime('%Y%m%d')) + 'f' + '.zip'
    file_dir = os.path.join(STATIC_DIR, node_name, day_dir_name, zip_file_name)
    unzip(file_dir, unzip_dir)


def get_FileSize(file_path):
    file_size = os.path.getsize(file_path)
    file_size = file_size/float(1024*1024)
    return round(file_size, 2)


def get_5_days():
    day_list = []
    for day in range(1, 6, 1):
        delta = datetime.timedelta(days=-day)
        n_days = now + delta
        backup_day = n_days.strftime('%Y%m%d') + 'f'
        day_list.append(backup_day)
    return day_list


def get_forms_day():
    forms_day = []
    for day in range(1, 6, 1):
        delta = datetime.timedelta(days=-day)
        n_days = now + delta
        backup_day = n_days.strftime('%-m-%d')
        forms_day.append(backup_day)
    return forms_day


def get_web_file_size_list(username, node_name):
    forms_day_list = get_forms_day()
    file_names = get_5_days()
    web_size_list = []
    for nums in range(0, 5, 1):
        dir_path = file_names[nums]
        forms_day = forms_day_list[nums]
        web_file_path = os.path.join(STATIC_DIR, node_name, dir_path, username) + '.web.7z.001'
        try:
            result = str(get_FileSize(web_file_path)) + ' M'
        except:
            result = '文件不存在'
        backup_dic = {'time': forms_day, 'size': result, 'download_path': web_file_path}
        web_size_list.append(backup_dic)
    return web_size_list


def get_sql_file_size_list(username, node_name):
    forms_day_list = get_forms_day()
    file_names = get_5_days()
    sql_size_list = []
    for nums in range(0, 5, 1):
        backup_dic = {}
        dir_path = file_names[nums]
        forms_day = forms_day_list[nums]
        web_file_path = os.path.join(STATIC_DIR, node_name, dir_path, username) + '.sql.7z.001'
        try:
            result = str(get_FileSize(web_file_path)) + ' M'
        except:
            result = '文件不存在'
        backup_dic = {'time': forms_day, 'size': result, 'download_path': web_file_path}
        sql_size_list.append(backup_dic)
    return sql_size_list








































# ROOT_DIR = '/Users/huyujie/Desktop/backup'
#
# node_id = 'node1'
#
# day_file_dir = os.path.join(ROOT_DIR, node_id, 'backup')
#
#
# def unzip_file(zip_src, dst_dir):
#     r = zipfile.is_zipfile(zip_src)
#     if r:
#         fz = zipfile.ZipFile(zip_src, 'r')
#         for file in fz.namelist():
#             fz.extract(file, dst_dir)
#     else:
#         print('This is not zip')
#
#



# 遍历生成 文件:路径 的字典

# file_dict = {}
#
#
# def get_FileDict(dir_path):
#     for filename in os.listdir(dir_path):
#         file_path = os.path.join(dir_path, filename)
#         file_dict.update({filename: file_path})
#     return file_dict
#
#
# all_dict = {}
#
# # get_FileDict('/Users/huyujie/Desktop/backup/node1/backup/20200113f')
#
# def match_file(f_dict, username):
#     pass