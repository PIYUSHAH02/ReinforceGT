payoffs = {
    ('C', 'C'): (3, 3),  # Both cooperate
    ('C', 'D'): (0, 5),  # Player 1 cooperates, Player 2 defects
    ('D', 'C'): (5, 0),  # Player 1 defects, Player 2 cooperates
    ('D', 'D'): (1, 1)   # Both defect
}

moves = ['C', 'D']

def is_nash_equilibrium(pair):
    """
    Check if a pair of moves (like ('C', 'C')) is a Nash Equilibrium.
    pair: A tuple like ('C', 'D') where first is Player 1's move, second is Player 2's.
    Returns: True if it's a Nash Equilibrium, False if not.
    """
    p1_move, p2_move = pair  # Split the pair into Player 1's and Player 2's moves
    
    # Check Player 1: Can they get more points by switching?
    p1_points = payoffs[(p1_move, p2_move)][0]  # Player 1's current points (first number)
    for other_move in moves:
        if other_move != p1_move:  # Try a different move for Player 1
            new_points = payoffs[(other_move, p2_move)][0]  # Points if Player 1 switches
            if new_points > p1_points:  # If they get more points by switching
                return False  # Not a Nash Equilibrium, Player 1 would switch
    
    # Check Player 2: Can they get more points by switching?
    p2_points = payoffs[(p1_move, p2_move)][1]  # Player 2's current points (second number)
    for other_move in moves:
        if other_move != p2_move:  # Try a different move for Player 2
            new_points = payoffs[(p1_move, other_move)][1]  # Points if Player 2 switches
            if new_points > p2_points:  # If they get more points by switching
                return False  # Not a Nash Equilibrium, Player 2 would switch
    
    return True  # Neither player wants to switch, so it's a Nash Equilibrium


all_pairs = [('C', 'C'), ('C', 'D'), ('D', 'C'), ('D', 'D')]
print("Checking all pairs for Pure Nash Equilibrium:")
nash_equilibria = []  # To store all Nash Equilibria
for pair in all_pairs:
    if is_nash_equilibrium(pair):
        nash_equilibria.append(pair)
        print(f"{pair} is a Pure Nash Equilibrium!")
    else:
        print(f"{pair} is NOT a Pure Nash Equilibrium.")

print("\nAll Pure Nash Equilibria:", nash_equilibria)