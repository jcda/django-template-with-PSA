from .base import *             # NOQA
import sys
import logging.config

from django.core.urlresolvers import reverse_lazy
from os.path import dirname, join, exists

## FOR THE MOMENT, THIS PART DOESNT WORK YET,  I WILL JUST USE THE VARIABLE UNDER THIS
#env_file = join(dirname(__file__), 'local.env')
#if exists(env_file):
#    environ.Env.read_env(str(env_file))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f+3+9(0%gc7ulm7(@jy*#p($*0cl1j0$8%)n^j8jgor=&z5fl5'
