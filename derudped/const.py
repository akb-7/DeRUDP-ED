MAX_BYTES = 90000 # 65535 should be less than receiver buffer size
MAX_PCKT_SIZE = 1460
POLL_INTERVAL = 0.1 # 10 polls / sec
HEADER_SIZE = 9
TIMEOUT = 0.2 # seconds
RWND = 10 # Retransmission window size (maximum no of packets to be retransmitted after timeout)
