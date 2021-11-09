from io import BytesIO
from datetime import datetime, time
import pickle


def create_task(name, due_date, required_time):
    return dict(name=name, due_date=due_date, required_time=required_time,
                finished=False)


def save_task(task, file):
    pickle.dump(task, file)


def load_task(file):
    return pickle.load(file)


def format_task(task):
    state = "完了" if task['finished'] else "未完了"
    format = "{state} {task[name]}: {task[due_date]: %Y-%m-%d}まで 予定所要時間 {task[required_time]}分"
    return format.format(task=task, state=state)


def finish_task(task):
    task['finished'] = True


def main():
    from datetime import datetime, time
    t = create_task("たすく", datetime(2020, 4, 1), time(0, 25))
    tasks = []
    tasks.append(t)
    out = BytesIO()
    save_task(tasks, out)
    out.seek(0)


if __name__ == '__main__':
    main()
