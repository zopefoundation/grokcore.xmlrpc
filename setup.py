from setuptools import setup, find_packages
import os

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
    'grokcore.view [security_publication]',
    'grokcore.view [test]',
    'zope.app.appsetup',
    'zope.app.wsgi',
    'zope.errorview',
    'zope.testing',
    ]

setup(
    name='grokcore.xmlrpc',
    version='1.2dev',
    author='Grok Team',
    author_email='grok-dev@zope.org',
    url='http://grok.zope.org',
    download_url='http://cheeseshop.python.org/pypi/grokcore.json/',
    description='XML-RPC View Component for Grok.',
    long_description=long_description,
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Framework :: Zope3',
        ],
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages=['grokcore'],
    include_package_data = True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'grokcore.component >= 2.5dev',
        'grokcore.security',
        'grokcore.view',
        'grokcore.traverser',
        'grokcore.content',
        'martian',
        'zope.component',
        'zope.interface',
        'zope.publisher',
        ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
)
