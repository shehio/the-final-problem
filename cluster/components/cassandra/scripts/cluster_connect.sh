export CASSANDRA_PASSWORD=$(kubectl get secret --namespace "default" my-cassandra -o jsonpath="{.data.cassandra-password}" | base64 -d)
kubectl run --namespace default my-cassandra-client --rm --tty -i --restart='Never'  --env CASSANDRA_PASSWORD=$CASSANDRA_PASSWORD  --image docker.io/bitnami/cassandra:4.1.5-debian-12-r2 -- bash
cqlsh -u cassandra -p $CASSANDRA_PASSWORD my-cassandra