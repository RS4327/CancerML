import setuptools


with open("README.md",'r',encoding='utf-8') as f:
    log_description=f.read()



__version__='0.0.0'

REPO_NAME='CancerML'
AUTHOR_USER_NAME='RS4327'
SRC_REPO='LinearRegression'
AUTHOR_EMAIL='raju.meenige@gmail.com'


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A Python package for NLTK APP',
    long_description=log_description,
    long_description_content='text/markdown',
    urs=f"https//github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    projct_urls={
        "Bug Tracker" :f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir={"":'src'},
    packages=setuptools.find_namespace_packages(where='src')
    )