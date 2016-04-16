#! /usr/bin/python
# -*- coding: utf-8 -*-

import luigi

from crawlers.bills import get_list as get_bill_list
import utils


class HourlyTasks(luigi.WrapperTask):
    # Runs every hour at 00 mins
    hour = luigi.DateHourParameter(default=utils.now())

    def requires(self):
        yield ScrapeBillList()


class ScrapeBillList(luigi.Task):

    def run(self):
        get_bill_list.pages()
