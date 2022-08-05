import os

from setuptools import find_packages
from setuptools import setup


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Download\n'
    '********\n'
)


tests_require = [
    'grokcore.view[security_publication]',
    'grokcore.view[test]',
    'zope.app.appsetup',
    'zope.app.wsgi[test]',
    'zope.errorview',
    'zope.testbrowser',
    'zope.testing',
]


setup(
    name='grokcore.xmlrpc',
    version='4.0.dev0',
    author='Grok Team',
    author_email='grok-dev@zope.org',
    url='http://grok.zope.org',
    download_url='http://cheeseshop.python.org/pypi/grokcore.json/',
    description='XML-RPC View Component for Grok.',
    long_description=long_description,
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Zope :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['grokcore'],
    include_package_data=True,
    zip_safe=False,
    python_requires='>= 3.6',
    install_requires=[
        'grokcore.component >= 2.5dev',
        'grokcore.content',
        'grokcore.security',
        'grokcore.traverser',
        'grokcore.view',
        'martian',
        'setuptools',
        'zope.component',
        'zope.interface',
        'zope.publisher',
    ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
)
