from django_q.tasks import async_task, result, schedule
from utils.new_slots import generate

def print_result(task): print(task.result)

def printer(*args):
    print('BRrrr')
    return "brrrr"

schedule('math.copysign',
         2, -2,
         hook='print_result',
         schedule_type='I')