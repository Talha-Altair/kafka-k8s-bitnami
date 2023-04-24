# Install Kafka with SASL authentication

helm install kafka bitnami/kafka -f values.yaml --version 21.4.5

## Configuration

You need to configure your Kafka client to access using SASL authentication.

- kafka_jaas.conf:

```txt
KafkaClient {
org.apache.kafka.common.security.scram.ScramLoginModule required
username="neone"
password="$(kubectl get secret kafka-jaas --namespace default -o jsonpath='{.data.client-passwords}' | base64 -d | cut -d , -f 1)";
};
```

- client.properties:

```txt
security.protocol=SASL_PLAINTEXT 
sasl.mechanism=SCRAM-SHA-256
```

Kafka Brokers domain: You will have a different external IP for each Kafka broker. You can get the list of external IPs using the command below:

```bash
echo "$(kubectl get svc --namespace default -l "app.kubernetes.io/name=kafka,app.kubernetes.io/instance=kafka,app.kubernetes.io/component=kafka,pod" -o jsonpath='{.items[*].status.loadBalancer.ingress[0].ip}' | tr ' ' '\n')"
```

Kafka Brokers port: 9092
