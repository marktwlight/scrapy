from apscheduler.schedulers.blocking import BlockingScheduler
from links import article_links, economia_links
from content import getContent
scheduler = BlockingScheduler()


print("开始执行每日任务")
print(article_links)

# 每天早上执行任务
# scheduler.add_job(getContent, 'interval', seconds=1, args=[article_links])

# scheduler.add_job(getContent, 'interval', seconds=1, args=[article_links])
scheduler.add_job(getContent, 'cron', hour=10, minute=28, args=[article_links])
scheduler.add_job(getContent, 'cron', hour=10,
                  minute=28, args=[economia_links])
scheduler.start()
