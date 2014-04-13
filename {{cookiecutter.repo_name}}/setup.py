from distutils.core import setup

setup(name='{{cookiecutter.repo_name}}',
        version='1.0',
        description='{{cookiecutter.description}}',
        author='{{cookiecutter.author}}',
        url='{{cookiecutter.url}}',
        author_email='{{cookiecutter.email}}',
        repo_names=['{{cookiecutter.repo_name}}'],
        install_requires=[
            ''
            ],
        classifiers=[
            'Programming Language :: Python',
            'License :: OSI Approved :: MIT License'
            ]
        )
