from setuptools import setup
setup(
  name = 'redash_client',
  packages = ['redash_client', 'redash_client.dashboards'],
  version = '0.1.9',
  description = 'A client for the re:dash API for stmo (https://sql.telemetry.mozilla.org)',
  author = 'Marina Samuel',
  author_email = 'msamuel@mozilla.com',
  url = 'https://github.com/mozilla/redash_client',
  keywords = ['redash', 'experiments', 'a/b tests'],
  classifiers = [],
  install_requires=[
    "boto3 == 1.4.4",
    "requests == 2.12.1",
    "python-slugify == 1.2.4",
  ]
)