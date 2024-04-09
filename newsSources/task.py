from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import contentFromNM
import contentFromPoder360
import contentFromSapo
# import contentFromGoal

scheduler = BlockingScheduler()
# scheduler = BackgroundScheduler()


print("开始执行每日任务")

# 所有需要执行的任务


def composite_job():
    # 按顺序执行多个任务函数
    # contentFromGoal.getContent()
    contentFromNM.getContent()
    contentFromPoder360.getContent()
    contentFromSapo.getContent()


# 每天早上执行任务
# scheduler.add_job(getContent, 'interval', seconds=1)

# scheduler.add_job(getContent, 'interval', seconds=1, args=[article_links])
scheduler.add_job(composite_job, 'cron', hour=8, minute=55)
# scheduler.add_job(getContent, 'cron', hour=11, minute=31)
scheduler.start()
