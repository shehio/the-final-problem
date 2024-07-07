import chess.pgn
import uuid
from datetime import datetime
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Cassandra connection details
CASSANDRA_HOSTS = ['127.0.0.1']
CASSANDRA_PORT = 9042
CASSANDRA_KEYSPACE = 'my_keyspace'
CASSANDRA_USERNAME = 'cassandra'
CASSANDRA_PASSWORD = '0taIgfmbx1'

# Connect to Cassandra
auth_provider = PlainTextAuthProvider(username=CASSANDRA_USERNAME, password=CASSANDRA_PASSWORD)
cluster = Cluster(CASSANDRA_HOSTS, port=CASSANDRA_PORT, auth_provider=auth_provider)
session = cluster.connect(CASSANDRA_KEYSPACE)

# Prepare statements
insert_game_stmt = session.prepare("""
    INSERT INTO games (game_id, player1_id, player2_id, start_time, end_time)
    VALUES (?, ?, ?, ?, ?)
""")
insert_move_stmt = session.prepare("""
    INSERT INTO moves (game_id, move_number, player_id, move, timestamp)
    VALUES (?, ?, ?, ?, ?)
""")

def parse_pgn_and_insert_to_cassandra(pgn_file_path):
    with open(pgn_file_path, 'r') as pgn_file:
        while True:
            game = chess.pgn.read_game(pgn_file)
            if game is None:
                break

            # Generate UUIDs for game and players
            game_id = uuid.uuid4()
            player1_id = uuid.uuid4()
            player2_id = uuid.uuid4()

            # Extract game headers
            headers = game.headers
            start_time = datetime.strptime(headers.get("Date", "1970.01.01"), "%Y.%m.%d")
            end_time = start_time  # Assuming end_time is the same as start_time for simplicity

            # Insert game data into the games table
            session.execute(insert_game_stmt, (game_id, player1_id, player2_id, start_time, end_time))

            # Insert moves data into the moves table
            board = game.board()
            move_number = 1
            for move in game.mainline_moves():
                session.execute(insert_move_stmt, (game_id, move_number, player1_id if move_number % 2 != 0 else player2_id, move.uci(), start_time))
                board.push(move)
                move_number += 1

if __name__ == "__main__":
    pgn_file_path = 'Fischer.pgn'
    parse_pgn_and_insert_to_cassandra(pgn_file_path)
