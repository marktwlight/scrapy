from apscheduler.schedulers.blocking import BlockingScheduler
import content
import urls
scheduler = BlockingScheduler()


def daily_task():
    print("执行每日任务")


urls = urls.urls
# 每天早上执行任务
# scheduler.add_job(content.getHtmlContent, 'interval', seconds=1, args=[urls])

scheduler.add_job(content.getHtmlContent, 'cron',hour=8, minute=20, args=[urls])
scheduler.start()
