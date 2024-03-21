import os

# 获取当前文件的绝对路径
current_file_path = os.path.abspath(__file__)

# 获取当前文件所在的文件夹路径
current_folder = os.path.dirname(current_file_path)

print("当前文件所在文件夹路径:", current_folder)
