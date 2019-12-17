# -*- coding: utf-8 -*-
import os
import time
import logging
import logging.handlers
import traceback
import cPickle
import struct
import SocketServer
from multiprocessing import Process
from other import handle_log


class LogRecordStreamHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        while True:
            try:
                chunk = self.connection.recv(4)
                if len(chunk) < 4:
                    break
                slen = struct.unpack(">L", chunk)[0]
                chunk = self.connection.recv(slen)
                while len(chunk) < slen:
                    chunk = chunk + self.connection.recv(slen - len(chunk))
                obj = self.unpickle(chunk)
                record = logging.makeLogRecord(obj)
                self.handle_log_record(record)

            except:
                break

    @classmethod
    def unpickle(cls, data):
        return cPickle.loads(data)

    def handle_log_record(self, record):
        if self.server.logname is not None:
            print "1"
            name = self.server.logname
        else:
            print "2"
            name = record.name
        print name
        logger = logging.getLogger(name)
        logger.handle(record)


class LogRecordSocketReceiver(SocketServer.ThreadingTCPServer):
    allow_reuse_address = 1

    def __init__(self, host='localhost', port=logging.handlers.DEFAULT_TCP_LOGGING_PORT, handler=LogRecordStreamHandler):
        SocketServer.ThreadingTCPServer.__init__(self, (host, port), handler)
        self.abort = 0
        self.timeout = 1
        self.logname = None

    def serve_until_stopped(self):
        import select
        abort = 0
        while not abort:
            rd, wr, ex = select.select([self.socket.fileno()], [], [], self.timeout)
            if rd:
                self.handle_request()
            abort = self.abort


def _log_listener_process(log_format, log_time_format, log_file):
    log_file = os.path.realpath(log_file)
    logging.basicConfig(level=logging.DEBUG,
                        format=log_format,
                        datefmt=log_time_format,
                        filename=log_file, filemode='a+')

    #Console log
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter(fmt=log_format, datefmt=log_time_format))
    logging.getLogger().addHandler(console)

    handler = logging.FileHandler("log.txt")
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(fmt=log_format, datefmt=log_time_format))
    logging.getLogger(name='123').addHandler(handler)



    tcp_server = LogRecordSocketReceiver()

    logging.debug('Log listener process started ...')
    tcp_server.serve_until_stopped()

class LogHelper:
    # 默认日志存储路径（相对于当前文件路径）
    default_log_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'logs')

    # 记录当前实际的日志所在目录
    current_log_path = ''

    # 记录当前实际的日志完整路径
    current_log_file = 'multi.log'

    # 日志文件内容格式
    log_format = '[%(asctime)s.%(msecs)03d][%(processName)s][%(levelname)s][%(filename)s:%(lineno)d] %(message)s'

    # 日志中时间格式
    log_time_format = '%Y%m%d %H:%M:%S'

    # 日志进程
    log_process = None

    def __init__(self):
        pass

    @staticmethod
    def print_console_log(level, message):
        print '--------------------------------------------------'
        if level == logging.WARN:
            level_str = '[WARN]'
        elif level == logging.ERROR:
            level_str = '[ERROR]'
        elif level == logging.FATAL:
            level_str = '[FATAL]'
        else:
            level_str = '[INFO]'
        print '\t%s %s' % (level_str, message)
        print '--------------------------------------------------'

    @staticmethod
    def init(clear_logs=True, log_path=''):
        #
        console = logging.StreamHandler()
        console.setLevel(logging.FATAL)
        logging.getLogger().addHandler(console)

        try:
            # 如果外部没有指定日志存储路径则默认在common同级路径存储
            if log_path == '':
                log_path = LogHelper.default_log_path
                if not os.path.exists(log_path):
                    os.makedirs(log_path)
            LogHelper.current_log_path = log_path

            # 清理旧的日志并初始化当前日志路径
            if clear_logs:
                LogHelper.clear_old_log_files()
            LogHelper.current_log_file = LogHelper._get_latest_log_file()

            socket_handler = logging.handlers.SocketHandler('localhost', logging.handlers.DEFAULT_TCP_LOGGING_PORT)
            logging.getLogger().setLevel(logging.DEBUG)
            logging.getLogger().addHandler(socket_handler)

            #
            LogHelper.start()

            logging.info("test")

        except Exception, ex:
            LogHelper.print_console_log(logging.FATAL, 'init() exception: %s' % str(ex))
            traceback.print_exc()

    @staticmethod
    def start():
        if LogHelper.log_process is None:
            LogHelper.log_process = Process(target=_log_listener_process, name='LogRecorder', args=(LogHelper.log_format, LogHelper.log_time_format, LogHelper.current_log_file))
            LogHelper.log_process.start()
        else:
            pass

    @staticmethod
    def stop():
        if LogHelper.log_process is None:
            pass
        else:
            LogHelper.log_process.terminate()
            LogHelper.log_process.join()

    @staticmethod
    def _get_latest_log_file():
        latest_log_file = ''
        try:
            if os.path.exists(LogHelper.current_log_path):
                for maindir, subdir, file_name_list in os.walk(LogHelper.current_log_path):
                    for file_name in file_name_list:
                        apath = os.path.join(maindir, file_name)
                        if apath > latest_log_file:
                            latest_log_file = apath

            if latest_log_file == '':
                latest_log_file = LogHelper.current_log_path + os.sep + 'system_'
                latest_log_file += time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time())) + '.log'

        except Exception, ex:
            logging.error('EXCEPTION: %s' % str(ex))
            traceback.print_exc()

        finally:
            return latest_log_file

    @staticmethod
    def get_log_file():
        return LogHelper.current_log_file

    @staticmethod
    def clear_old_log_files():
        if not os.path.exists(LogHelper.current_log_path):
            logging.warning('clear_old_log_files() Not exist: %s' % LogHelper.current_log_path)
            return

        try:
            for maindir, subdir, file_name_list in os.walk(LogHelper.current_log_path):
                for file_name in file_name_list:
                    apath = os.path.join(maindir, file_name)
                    if apath != LogHelper.current_log_file:
                        logging.info('DEL -> %s' % str(apath))
                        os.remove(apath)
                    else:
                        with open(LogHelper.current_log_file, 'w') as f:
                            f.write('')

            logging.debug('Clear log done.')

        except Exception, ex:
            logging.error('EXCEPTION: %s' % str(ex))
            traceback.print_exc()


def test():
    worker = Process(target=_log_listener_process, name='LogRecorder',
            args=(LogHelper.log_format,
                  LogHelper.log_time_format,
                  LogHelper.current_log_file)
            )

    worker.start()

    time.sleep(5)
    worker2 = Process(target=handle_log,name='handle')

    worker2.start()

    worker2.join()

    #worker.terminate()


def main():
    logging.basicConfig(
        format="%(relativeCreated)5d %(name)-15s %(levelname)-8s %(message)s")
    tcpserver = LogRecordSocketReceiver()
    print "About to start TCP server..."
    tcpserver.serve_until_stopped()

if __name__ == '__main__':
    #LogHelper.init()
    # main()
    test()
