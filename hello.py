from datetime import datetime, time


def create_task(name, due_date, required_time):
    return dict(name=name, due_date=due_date, required_time=required_time,
                finished=False)


def format_task(task):
    state = "完了" if task['finished'] else "未完了"
    format = "{state} {task[name]}: {task[due_date]: % Y-%m-%d}まで 予定所要時間 {task[required_time]}分"
    return format.format(task=task, state=state)


def finish_task(task):
    task['finished'] = True


def main():
    t = create_task("たすく", datetime(2020, 4, 1), time(0, 25))
    finish_task(t)
    t['finished']
    print(format_task(t))


if __name__ == '__main__':
    main()
