import os
from datetime import timedelta

redis_url = 'redis://{host}:{port}/'.format(
    host=os.environ.get('REDIS_HOST'),
    port=os.environ.get('REDIS_PORT')
)

class Config(object):
    redbeat_redis_url = ''.join([redis_url, os.environ.get('REDBEAT_DB')])
    beat_scheduler = 'redbeat.RedBeatScheduler'

    # 使用rabbitmq作为消息代理
    broker_url = ''.join([redis_url, os.environ.get('BROKER_DB')])
    result_backend = ''.join([redis_url, os.environ.get('RESULT_DB')])
    task_serializer = 'msgpack'  # 任务序列化和反序列化使用msgpack方案
    result_serializer = 'json'  # 读取任务结果要求性能不高，使用可读性更好的JSON
    result_expires = 60 * 60 * 24  # 任务任务过期时间
    accept_content = ['json', 'msgpack']  # 指点接受的内容类型
    timezone = 'UTC'  # 设置时区
    enable_utc = True  # 开启utc
    # task_track_started = True  # 任务跟踪
    # worker_hijack_root_logger = True  # 禁用log root 清理

    beat_schedule = {
        'test': {
            'task': 'task.schedule_async',
            # 'schedule': crontab('*')
            'schedule': timedelta(seconds=1),
        }
    }
