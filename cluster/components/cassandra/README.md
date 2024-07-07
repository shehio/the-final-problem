1. Create the cassandra cluster: `./scripts/cluster_provision`
2. Get password: `echo $(kubectl get secret --namespace "default" my-cassandra -o jsonpath="{.data.cassandra-password}" | base64 -d)`
3. Add password to `cassandra-migrate.yaml`
4. Run `cassandra-migrate migrate -c cassandra-migrate.yml` to migrate the schema
5. Run `kubectl port-forward --namespace default svc/my-cassandra-2 9042:9042 & cd demo && python migrate_pgn.py`