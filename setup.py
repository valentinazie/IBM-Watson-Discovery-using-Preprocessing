from setuptools import setup, find_packages

setup(
    name='document_reformatting_using_IBM_WD',  # Replace with your project's name
    version='0.1.0',  # The current version of your project
    author='Valentina',  # Your name
    author_email='Eunji.Kim2@ibm.com',  # Your email
    description='A short description of the project.',  # A brief description of your project
    long_description=open('README.md').read(),  # A long description from your README.md
    # url='https://github.com/yourusername/yourproject',  # The URL to your project's repository
    packages=find_packages(),  # This will find all packages in your project
    install_requires=[  # List all of your project's dependencies here
        "aiohttp",
        "aiosignal",
        "annotated-types",
        "anyio",
        "attrs",
        "certifi",
        "charset-normalizer",
        "dataclasses-json",
        "frozenlist",
        "ibm-cos-sdk",
        "ibm-cos-sdk-core",
        "ibm-cos-sdk-s3transfer",
        "ibm-watson-machine-learning",
        "idna",
        "importlib-metadata",
        "jmespath",
        "jsonpatch",
        "jsonpointer",
        "langchain",
        "langchain-community",
        "langchain-core",
        "langsmith",
        "lomond",
        "marshmallow",
        "multidict",
        "mypy-extensions",
        "numpy",
        "packaging",
        "pandas",
        "pydantic",
        "pydantic-core",
        "python-dateutil",
        "pytz",
        "PyYAML",
        "requests",
        "rouge",
        "six",
        "sniffio",
        "SQLAlchemy",
        "tabulate",
        "tenacity",
        "tqdm",
        "typing-inspect",
        "typing-extensions",
        "urllib3",
        "yarl",
        "zipp",
        "python-dotenv",
        "ibm_watson",
        "beautifulsoup4",
    ],
    classifiers=[  # Classifiers help users find your project by categorizing it
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',  # Your project's Python version requirements
)
