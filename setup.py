"""The setup for Mailroom distribution."""

from setuptools import setup

setup(
    name='mailroom',
    description='Manage donation list and automate thank-you emails.',
    version=0.1,
    author='Jordan Schatzman, Rick Valenzuela',
    author_email='j.schatzman@outlook.com, rv@rickv.com',
    license='MIT',
    package_dir={'': 'src'},
    py_modules=['mailroom'],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
)
