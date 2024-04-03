from apscheduler.schedulers.blocking import BlockingScheduler
import content
import urls
scheduler = BlockingScheduler()


print("开始执行每日任务")


urls = urls.urls
# # 每天早上执行任务
# scheduler.add_job(content.getHtmlContent, 'interval', hour=16,minute=30, args=[urls])

scheduler.add_job(content.getHtmlContent, 'cron',hour=11, minute=38, args=[urls])
scheduler.start()
