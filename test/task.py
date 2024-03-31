from apscheduler.schedulers.blocking import BlockingScheduler

i = 1


def daily_task(i):
    print("执行每日任务", i)


scheduler = BlockingScheduler()

# 使用 interval 触发器，每秒执行一次任务
scheduler.add_job(daily_task, 'interval', seconds=1, args=[i])

scheduler.start()
