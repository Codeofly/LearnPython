from . import versions
from ..cmd import manage
__all__ = ['get']
def get():
    print('from policy.py')

versions.create_resource('userinfo')
manage.main()