import logging

class ALog(object):
    def __init__(self):
        """Do nothing, by default."""
        m_logger = logging.getLogger()
        m_hdlr = logging.FileHandler('automake.log')
        m_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        m_hdlr.setFormatter(m_formatter)
        m_logger.addHandler(m_hdlr)
        m_logger.setLevel(logging.NOTSET)
       
    @staticmethod 
    def e(msg):
        m_logger.error(msg)
        m_hdlr.flush()
#m_logger.removeHandler(m_hdlr)
#        m_hdlr.close()
	@staticmethod
	def w(msg):


if __name__=="__main__":
	ALog.log("ErrorTest")
