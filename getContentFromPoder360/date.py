from datetime import datetime,timedelta


#葡萄牙语月份简写
month_mapping = {
    'jan': 'Jan',
    'fev': 'Feb',
    'mar': 'Mar',
    'abr': 'Apr',
    'mai': 'May',
    'jun': 'Jun',
    'jul': 'Jul',
    'ago': 'Aug',
    'set': 'Sep',
    'out': 'Oct',
    'nov': 'Nov',
    'dez': 'Dec'
}

# 获取当前日期
current_date = datetime.now()

# 格式化日期为 YYYY-MM-DD 样式
formatted_date = current_date.strftime('%Y-%m-%d')

print("今天的日期是:", formatted_date)