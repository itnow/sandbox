Start dev environment:
    
    pipenv --python 3.6
    pipenv install --dev
    
    # run each in its own terminal
    source run_redis.sh
    source run_celery.sh
    source run_app.sh