#!/bin/bash

# Java 설치
sudo yum install -y java-1.8.0-openjdk

# Kafka 다운로드 및 설치
cd /opt
wget https://downloads.apache.org/kafka/3.4.0/kafka_2.13-3.4.0.tgz
tar -xzf kafka_2.13-3.4.0.tgz

# ZooKeeper 실행
cd /opt/kafka_2.13-3.4.0
bin/zookeeper-server-start.sh -daemon config/zookeeper.properties

# Kafka 서버 실행
bin/kafka-server-start.sh -daemon config/server.properties
