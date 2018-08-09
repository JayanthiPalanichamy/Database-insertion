import psycopg2
import subprocess
def connect():
    proc = subprocess.Popen('heroku config:get DATABASE_URL -a test-redbus', stdout=subprocess.PIPE, shell=True)
    db_url = proc.stdout.read().decode('utf-8').strip() + '?sslmode=require'
    return psycopg2.connect(db_url)
    
