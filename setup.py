from setuptools import setup

setup(
    name='cisco_router_uptime_netconf',
    version='1.0',
    packages=[''],
    url='https://github.com/djordjevulovic/CiscoRouterUptimeNETCONF',
    license='',
    author='dvulovic',
    author_email='dvulovic@cisco.com',
    description='Print uptime of Cisco routers using NETCONF',
    install_requires=[
          'lxml',
          'nccclient',
          'dateutil'
      ]
)
