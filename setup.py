try:
    from setuptools import setup, find_packages
    setup(
        name="cri_manager",
        version="1.0",
        package_dir={'':'.'},
        packages=find_packages(),
        scripts=['manager.py'],
        install_requires=['docker>=3.7.2'],
        package_data={
            '':['*.txt','*.rst']
        },
        author="Xavier AMORENA",
        author_email="xavier.amorena@labri.fr",
        description="Container Runtimes Interface Manager",
        keywords="Docker, Server",
        url="https://github.com/xamorena/cri_manager.git",
        project_urls={
            "Source Code":"https://github.com/xamorena/cri_manager.git"
        },
        classifiers=[
            'License :: OSI Approved :: Python Software Foundation License'
        ]
    )
except Exception as err:
    import logging
    logging.error("OUPS! sorry, an error occur ... %s", str(err))
