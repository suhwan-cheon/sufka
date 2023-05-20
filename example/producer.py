from confluent_kafka import Producer

# Kafka 브로커 서버의 호스트와 포트 설정
bootstrap_servers = 'localhost:9092'

# 토픽 이름 설정
topic = 'sufka-topic1'

# Kafka Producer 설정
producer = Producer({'bootstrap.servers': bootstrap_servers})

# 메시지 전송 콜백 함수
def delivery_callback(err, msg):
    if err is not None:
        print(f'메시지 전송 실패: {err}')
    else:
        print(f'메시지 전송 성공: {msg.topic()} [{msg.partition()}]')

# 메시지 전송
for i in range(10):
    message = f'메시지 {i+1}'
    producer.produce(topic, value=message, callback=delivery_callback)

# 모든 메시지 전송 완료 대기
producer.flush()
