USE chess;

CREATE TABLE games (
    game_id UUID PRIMARY KEY,
    player1_id UUID,
    player2_id UUID,
    start_time TIMESTAMP,
    end_time TIMESTAMP
);

CREATE TABLE moves (
    game_id UUID,
    move_number INT,
    player_id UUID,
    move TEXT,
    timestamp TIMESTAMP,
    PRIMARY KEY (game_id, move_number)
);
