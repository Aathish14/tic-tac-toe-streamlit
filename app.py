import streamlit as st

st.set_page_config(page_title="Tic Tac Toe", layout="centered")

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.score = {"X": 0, "O": 0, "Draws": 0}

def check_winner(board):
    combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in combos:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if all(cell != "" for cell in board):
        return "Draw"
    return None

def restart_game():
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None

st.title("🎮 Tic Tac Toe - Web App")
st.markdown("Play Tic Tac Toe in your browser! Two-player mode.")

# Scoreboard
st.sidebar.header("📊 Scoreboard")
st.sidebar.write(f"Player X: {st.session_state.score['X']} wins")
st.sidebar.write(f"Player O: {st.session_state.score['O']} wins")
st.sidebar.write(f"Draws: {st.session_state.score['Draws']}")

# Display 3x3 grid
cols = st.columns(3)
for i in range(3):
    for j in range(3):
        idx = i * 3 + j
        if st.session_state.board[idx] == "":
            if cols[j].button(" ", key=idx):
                if not st.session_state.winner:
                    st.session_state.board[idx] = st.session_state.current_player
                    st.session_state.winner = check_winner(st.session_state.board)
                    if st.session_state.winner:
                        if st.session_state.winner in ["X", "O"]:
                            st.session_state.score[st.session_state.winner] += 1
                        else:
                            st.session_state.score["Draws"] += 1
                    else:
                        st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
        else:
            cols[j].button(st.session_state.board[idx], key=idx, disabled=True)

# Show game status
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.success("🤝 It's a draw!")
    else:
        st.success(f"🏆 Player {st.session_state.winner} wins!")

# Restart button
if st.button("🔄 Restart Game"):
    restart_game()