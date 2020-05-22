from django_cron import CronJobBase, Schedule

from .models import Post


class ClearVotes(CronJobBase):
    """Once per day this function reset post`s votes"""
    RUN_AT_TIMES = ['3:59']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'post.cron.ClearVotes'

    def do(self):
        posts = Post.objects.all()
        for post in posts:
            post.votes.clear()
