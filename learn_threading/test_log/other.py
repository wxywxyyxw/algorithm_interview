import os
import logging, logging.handlers
def handle_log():
    rootLogger = logging.getLogger('123')
    rootLogger.setLevel(logging.DEBUG)
    socketHandler = logging.handlers.SocketHandler('localhost',
                        logging.handlers.DEFAULT_TCP_LOGGING_PORT)
    # don't bother with a formatter, since a socket handler sends the event as
    # an unformatted pickle
    rootLogger.addHandler(socketHandler)

    # Now, we can log to the root logger, or any other logger. First the root...
    logging.info('Jackdaws love my big sphinx of quartz.')

    #print os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'logs')

handle_log()

