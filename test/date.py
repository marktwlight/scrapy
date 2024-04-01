from datetime import datetime

# 定义月份缩写的映射关系
month_abbr = {
    "jan": "01",
    "fev": "02",
    "mar": "03",
    "apr": "04",
    "may": "05",
    "jun": "06",
    "jul": "07",
    "aug": "08",
    "sep": "09",
    "oct": "10",
    "nov": "11",
    "dec": "12"
}

# 定义日期字符串
date_str = "14.fev.2024"

# 解析日期字符串
date_parts = date_str.split('.')
day = int(date_parts[0])
month = month_abbr[date_parts[1].lower()]  # 将月份缩写转换为小写，并在映射关系中查找对应的数字
year = int(date_parts[2])

# 构建日期对象
date = datetime(year, int(month), day)

# 打印日期对象
print(date)
