from invoke import task

@task
def init(context):
    print('Initiating environment')
    context.run('source ./.venv/bin/activate')

@task
def run(context):
    context.run('python bot.py')