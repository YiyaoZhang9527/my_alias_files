
from datetime import datetime
from enum import Enum

# color code, add your own color here if you need extra
class Color(Enum):
    WHITE = 0
    BLACK =30
    BLUE =34
    GREEN =32
    CYAN =36
    RED =31
    PURPLE =35
    YELLOW =33
    # BROWN

class LogLevel(Enum):
    CRITICAL = 'CRITICAL'
    ERROR = 'ERROR'
    WARN = 'WARN'
    INFO = 'INFO'
    DEBUG = 'DEBUG'
    SILLY = 'SILLY'
    PASS = 'PASS'

log_color_dict = {}
log_color_dict[LogLevel.CRITICAL] = Color.CYAN
log_color_dict[LogLevel.ERROR] = Color.RED
log_color_dict[LogLevel.WARN] = Color.BLUE
log_color_dict[LogLevel.INFO] = Color.YELLOW
log_color_dict[LogLevel.DEBUG] = Color.PURPLE
log_color_dict[LogLevel.SILLY] = Color.BLACK
log_color_dict[LogLevel.PASS] = Color.GREEN

def print_color(content: str, color: Color = Color.WHITE):
    print(f"\033[0;{color.value}m{content}\033[0m")

def log(content: str, level: LogLevel = LogLevel.DEBUG):
    print_color(f'{datetime.now()} - [{level.value}] - {content}', log_color_dict[level])


if __name__ == '__main__':
    log('LogLevel.CRITICAL', LogLevel.CRITICAL)
    log('LogLevel.ERROR', LogLevel.ERROR)
    log('LogLevel.WARN', LogLevel.WARN)
    log('LogLevel.PASS', LogLevel.PASS)
    log("LogLevel.INFO",LogLevel.INFO)
    log("LogLevel.DEBUG",LogLevel.DEBUG)
    log("LogLevel.SILLY",LogLevel.SILLY)
    

