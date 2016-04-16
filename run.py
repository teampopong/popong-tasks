#! /usr/bin/python
# -*- coding: utf-8 -*-

import luigi

from crawlers.bills import get_list as get_bill_list


class ScrapeBillList(luigi.Task):

    def run(self):
        get_bill_list.pages()
