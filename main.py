#-*-coding: utf-8
from indeed import get_jobs as indeed_get_jobs
from sof import get_jobs as sof_get_jobs
from save import save_to_file

so_jobs = sof_get_jobs()
indeed_jobs = indeed_get_jobs()
jobs = indeed_jobs
save_to_file(jobs)
