from kafka import KafkaProducer

bootstrap_servers = []

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    sasl_mechanism="SCRAM-SHA-256",
    sasl_plain_username="altair",
    sasl_plain_password="muchsecure",
    security_protocol="SASL_PLAINTEXT"
)

producer.send("auth", b"auth, World!")

producer.send("auth", key=b"auth-two", value=b"This is auth-Python")

producer.flush()