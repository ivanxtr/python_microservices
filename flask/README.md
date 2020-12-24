# Documentation

## Flask migration

```
docker-compose up exec backend sh
python manager.py db init
python manager.py db migrate
python manager.py db upgrade
```

## Run Consumer
```
python consumer.py
```

## Build the Queue
```
docker-compose up --build
docker-compose up
```

## See the DB Logs
```
docker-compose up -d db
```
