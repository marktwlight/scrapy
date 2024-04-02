from datetime import datetime

# 获取当前日期
current_date = datetime.now()

# 格式化日期为 YYYY-MM-DD 样式
formatted_date = current_date.strftime('%Y-%m-%d')

print("今天的日期是:", formatted_date)
