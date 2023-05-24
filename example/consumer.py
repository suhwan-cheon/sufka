from confluent_kafka import Consumer, KafkaException

# Kafka 클러스터의 부트스트랩 서버 주소
bootstrap_servers = 'localhost:9092'

# Kafka 토픽
topic = 'sufka-topic1'

# Kafka 컨슈머 설정
conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'your_consumer_group_id',
    'auto.offset.reset': 'earliest'
}

# 컨슈머 생성
consumer = Consumer(conf)

# 토픽 구독
consumer.subscribe([topic])

# 메시지 소비 루프
try:
    while True:
        msg = consumer.poll(1.0)  # 1초마다 메시지 폴링
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        else:
            print(f'Received message: {msg.value().decode("utf-8")}')
except KeyboardInterrupt:
    pass
finally:
    # 컨슈머 종료
    consumer.close()
