CREATE KEYSPACE chess
WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 3
};
