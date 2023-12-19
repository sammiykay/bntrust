from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from .tasks import delete_old_data

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')

# Schedule the job to run once a day
scheduler.add_job(delete_old_data, 'interval', days=1)

scheduler.start()
