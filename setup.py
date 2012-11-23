from setuptools import find_packages
from setuptools import setup


setup(
    name='slt.policy',
    version='0.4',
    description="Turns plone site into SLT shopping site.",
    long_description=open("README.rst").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@abita.fi',
    url='http://www.sll.fi/kauppa',
    license='None-free',
    # packages=find_packages(exclude=['ez_setup']),
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['slt'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Products.CMFPlone>=4.2'
        'abita.development',
        'five.pt',
        'hexagonit.socialbutton',
        'hexagonit.testing',
        'setuptools',
        'sll.locales',
        'slt.theme'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
