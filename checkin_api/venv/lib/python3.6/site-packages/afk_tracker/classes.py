#!/usr/bin/env python
import datetime
from afk_tracker.models import Afk
import public

@public.add
class Range:
    """Range class. attr: `started_at`, `finished_at`. properties: `max_afk`, `minutes`"""
    def __init__(self, started_at, finished_at):
        self.started_at = started_at
        self.finished_at = finished_at
        self.load()

    def load(self):
        self.rows = Afk.objects.filter(
            created_at__gt=self.started_at,
            created_at__lt=self.finished_at,
        ).all()
        return self

    @property
    def min_afk(self):
        if self.rows:
            return min(map(lambda m: m.afk, self.rows))

    @property
    def max_afk(self):
        if self.rows:
            return max(map(lambda m: m.afk, self.rows))


@public.add
class Minute(Range):
    """Minute class. attr: `started_at`, `finished_at`. properties: `available`, `min_afk`, `max_afk`"""

    @property
    def available(self):
        return bool(len(self.rows))

    def __str__(self):
        started_at = self.started_at.strftime('%Y-%m-%d %H:%M:%S')
        finished_at = self.finished_at.strftime('%Y-%m-%d %H:%M:%S')
        return "<Minute started=\"%s\" finished=\"%s\" min_afk=%s max_afk=%s>" % (started_at, finished_at, self.min_afk, self.max_afk)

    def __repr__(self):
        return self.__str__()


@public.add
class Hour(Range):
    """Hour class. attr: `started_at`, `finished_at`. properties: `available`, `min_afk`, `max_afk`, `minutes`"""

    def __init__(self, finished_at=None):
        if not finished_at:
            finished_at = datetime.datetime.now()
        started_at = finished_at - datetime.timedelta(hours=1)
        Range.__init__(self, started_at, finished_at)

    @property
    def minutes(self):
        result = []
        for i in reversed(range(0, 60)):
            finished_at = self.finished_at - datetime.timedelta(minutes=i)
            started_at = finished_at - datetime.timedelta(minutes=1)
            minute = Minute(started_at, finished_at)
            result.append(minute)
        return result

    @property
    def min_afk(self):
        minutes = list(filter(lambda m: m.available, self.minutes))
        if minutes:
            return max(map(lambda m: m.min_afk, minutes))

    @property
    def max_afk(self):
        minutes = list(filter(lambda m: m.available, self.minutes))
        if minutes:
            return max(map(lambda m: m.min_afk, minutes))

    def __str__(self):
        started_at = self.started_at.strftime('%Y-%m-%d %H:%M:%S')
        finished_at = self.finished_at.strftime('%Y-%m-%d %H:%M:%S')
        return "<Hour started=\"%s\" finished=\"%s\">" % (started_at, finished_at)

    def __repr__(self):
        return self.__str__()
