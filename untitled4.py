# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 19:01:02 2020

@author: computer
"""

import glassdoor_scraper as gs
import pandas as pd
path="C:/Users/computer/New folder/chromedriver"

df= gs.get_jobs("data science",15,False,path,15)