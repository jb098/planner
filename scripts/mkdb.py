#!/usr/bin/env python

from datetime import date
from os.path import exists

from planner.config import (
    TEAM_NAME, TEAM_CAPACITY, TEAM_REVENUE_CAP, TEAM_DEVMAX, TEAM_RESEARCH_MAX,
    TEAM_COST, LIVEDBPATH
)
from planner.model import Iteration
from planner.model.connect import new_database, LiveSession


def static_live_data():
    session = LiveSession()
    for d in [date(2015, 1, 5), date(2015, 1, 19), date(2015, 2, 2),
              date(2015, 2, 16), date(2015, 3, 2), date(2015, 3, 16),
              date(2015, 3, 30), date(2015, 4, 13), date(2015, 4, 27),
              date(2015, 5, 11), date(2015, 5, 25), date(2015, 6, 8),
              date(2015, 6, 22), date(2015, 7, 6), date(2015, 7, 20),
              date(2015, 8, 3), date(2015, 8, 17), date(2015, 8, 31),
              date(2015, 9, 14), date(2015, 9, 28), date(2015, 10, 12),
              date(2015, 10, 26), date(2015, 11, 9), date(2015, 11, 23),
              date(2015, 12, 7), date(2015, 12, 21)]:
        session.add(Iteration(startdate=d))
        session.add(Team(name=TEAM_NAME, cost=TEAM_COST,
                         capacity=TEAM_CAPACITY, devmax=TEAM_DEVMAX,
                         researchmax=TEAM_RESEARCH_MAX,
                         revenuecap=TEAM_REVENUE_CAP)
        session.commit()
        session.close()


if __name__ == '__main__':
    if not exists(LIVEDBPATH):
        new_database(LIVEDBPATH)
        static_live_data()
    print "DB created"
