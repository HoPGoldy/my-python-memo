"""
任务调度器
可以实现定时任务

安装:
内置模块，无需安装

参考:
中文文档 https://docs.python.org/zh-cn/3/library/sched.html
"""

import time, sched, datetime

# 重试间隔（秒）
RETRY_INTERVAL = 200

# 新建调度器
s = sched.scheduler(time.time, time.sleep)


def get_task_interval():
    """获取现在到明天零点的秒间隔

    Return:
        number: 现在到明天零点的秒数
    """
    # 获取现在的秒时间戳
    now_time_stamp = int(time.time())
    # 获取明天的秒时间戳
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow_time_stamp = int(time.mktime(tomorrow.timetuple()))
    # 获取明天零点多一点的秒时间戳
    tomorrow_time_stamp = int(tomorrow_time_stamp / 1000) * 1000 + 1

    return tomorrow_time_stamp - now_time_stamp


#被调度触发的函数
def task(msg):
    """执行绘制任务
    若成功执行完绘制任务则第二天零点再次绘制
    否则间隔 RETRY_INTERVAL 秒后重试
    """
    try:
        print(f'当前时间 {time.time()} 输出 {msg}')
        
        # 如果正常绘制完成则安排下一次绘制任务
        s.enter(get_task_interval(), 0, task, ('task restart', ))
        print('\n绘制完成，将在次日 0 点重新进行绘制，请确保本任务在后台运行。\n')
    
    # 绘制异常则尝试重试
    except Exception as err:
        print(f'任务出现异常，将在 {RETRY_INTERVAL} 秒后重试:\n', err)
        s.enter(RETRY_INTERVAL, 0, task, ('task retry', ))


if __name__ == "__main__":
    s.enter(0, 0, task, ('task start', ))
    s.run()