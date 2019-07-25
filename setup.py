from setuptools import setup

setup(
   name='michael',
   version='0.1',
   description='A/B testing and multi-armed bandit made easy',
   author='Charin Polpanumas',
   author_email='charin@central.tech',
   packages=['michael'],  #same as name
   install_requires=['plotnine','numpy','pandas'], #external packages as dependencies
)
