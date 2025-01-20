from invoke import task, run, Collection


@task(default=True)
def default(ctx):
    # Get a list of tasks
    tasks = sorted(ns.tasks.keys())
    # Display tasks and prompt user
    [print(f"{i}: {task_name}") for i, task_name in enumerate(tasks, 1)]
    choice = int(input("Enter the number of your choice: "))
    ctx.run(f"invoke {tasks[choice - 1]}")


@task
def init(c):
    project_name = input("Enter your project name: ")
    c.run(f"Initialize-Project -ProjectName {project_name}")


@task
def docs(c):
    c.run("mkdocs build")


@task
def commit(c, message="Initial commit"):
    c.run("git add .")
    c.run(f"git commit -m '{message}'")


@task
def clean(c):
    c.run("Remove-Item -Recurse -Force dist, build, *.egg-info")


ns = Collection(default, init, docs, commit, clean)
