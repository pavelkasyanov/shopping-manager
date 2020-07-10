import logging

logger = logging.getLogger()

logging.basicConfig(format=u'%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.DEBUG
                    # ,filename=log_file_name
                    )
