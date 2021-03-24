# Ubuntu dev environment
### Install system dependencies
```
sudo apt install python-mysqldb python3.8-dev
```

### Activate python virtual environment
```
source venv/bin/activate
```

### Create config.ini file to store sensitive data
```
python configuration.py
```

### Install python dependencies
```
pip install -r requirements.txt
```

### DB commands
```
django-admin startproject admin
cd admin

docker-compose up
docker-compose exec backend sh
    python manage.py startapp products
    # paste modified files to directories admin and products
    # use sudo \cp -r
    python manage.py makemigration
    python manage.py migrate    
    sudo rm db.sqlite3
    # paste serializers.py
```