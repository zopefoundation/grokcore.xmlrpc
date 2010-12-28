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
    'grokcore.view [test]',
    'grokcore.view [security_publication]',
    'zope.app.wsgi',
    'zope.app.appsetup',
    'zope.app.http',
    'zope.testing',
    ]

setup(
    name='grokcore.xmlrpc',
    version='0.1',
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
        'grokcore.component',
        'grokcore.security',
        'grokcore.view',
        'grokcore.traverser',
        'grokcore.content',
        'martian',
        'simplejson',
        'zope.component',
        'zope.interface',
        'zope.publisher',
        ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
)
