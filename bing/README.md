## Setup

Create settings file and add your API key:

```
cat settings.ini
[Bing]
Key=<your api key>
```

```
sudo apt-get install python-setuptools
wget https://fedorahosted.org/releases/s/u/suds/python-suds-0.3.7.tar.gz
tar -xzf python-suds-0.3.7.tar.gz
cd python-suds-0.3.7
sudo python setup.py install
```

### Install python-dev (needed to build MySQL-Python)

```
sudo apt-get install python-dev
sudo apt-get install libmysqlclient-dev
```

### Download MySQL-python

```
wget http://downloads.sourceforge.net/project/mysql-python/mysql-python/1.2.3/MySQL-python-1.2.3.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fmysql-python%2F&ts=1340730391&use_mirror=superb-sea2 -o MySQL-python-1.2.3.tar.gz
tar xzf MySQL-python-1.2.3.tar.gz
cd MySQL-python-1.2.3
sudo python setup.py build
sudo python setup.py install
```

