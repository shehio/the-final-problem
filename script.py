from kazoo.client import KazooClient

# Replace these with your ZooKeeper server details
hosts = ["{ip1}:2181", "{ip2}:2181", "{ip3}:2181"]
path = "/trying"
data = b"shehioshehio"

# Create a ZooKeeper client connection
zk = KazooClient(hosts=hosts)
zk.start()

# Create the znode
created = zk.create(path, data)

if created:
    print(f"Znode '{path}' created successfully!")
else:
    print(f"Failed to create znode '{path}'.")

# Close the connection
zk.stop()
