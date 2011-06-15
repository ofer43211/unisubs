from celery.decorators import periodic_task
from statistic import st_sub_fetch_handler, st_video_view_handler, st_widget_view_statistic
from datetime import timedelta

@periodic_task(run_every=timedelta(hours=2))
def update_statistic(*args, **kwargs):
    count = st_sub_fetch_handler.migrate()
    count = st_video_view_handler.migrate()
    count = st_widget_view_statistic.migrate()
