from distutils.core import setup
setup(
  name = 'oliver_prefect_kedro_ii',         
  packages = ['oliver_prefect_kedro_ii'], 
  version = '0.2.1', 
  license='MIT',     
  description = 'Prefect and Kedro package for Oliverto deployments',   
  author = 'OTH JG',                
  author_email = 'jgerstein@olivetreeholdings.com',      
  url = 'https://github.com/oth-jonathan-gerstein/oliver_prefect_kedro_ii',   
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['KEDRO', 'PREFECT', 'ETL', 'OLIVERTO'],   
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)