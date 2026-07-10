1. Create the cassandra cluster: `./scripts/cluster_provision.sh`
2. Fetch the cluster-generated password and store it in 1Password (one time, or whenever the cluster is reprovisioned):
   ```sh
   op item edit the-final-problem-cassandra \
     "password=$(kubectl get secret --namespace default my-cassandra -o jsonpath='{.data.cassandra-password}' | base64 -d)"
   ```
3. Add the password to `cassandra-migrate.yaml`
4. Run `cassandra-migrate migrate -c cassandra-migrate.yaml` to migrate the schema
5. Run the migration, letting `op run` inject the password from 1Password (nothing secret touches disk):
   ```sh
   kubectl port-forward --namespace default svc/my-cassandra-2 9042:9042 &
   cd demo && op run --env-file=cassandra.env -- python migrate_pgn.py
   ```
   `cassandra.env` holds only the `op://Private/the-final-problem-cassandra/password` reference;
   `migrate_pgn.py` reads the resolved value from `CASSANDRA_PASSWORD`. Requires the
   [1Password CLI](https://developer.1password.com/docs/cli/) signed in.
