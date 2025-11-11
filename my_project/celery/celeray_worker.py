from my_project.celery.tasks import celery_app
#celery -A celery_worker.celery_app worker --loglevel=info