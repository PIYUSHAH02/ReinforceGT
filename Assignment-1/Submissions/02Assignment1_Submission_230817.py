payoffs = {
    ('Bach', 'Bach'): (2, 1),        # Both pick Bach
    ('Bach', 'Stravinsky'): (0, 0),  # Player 1 picks Bach, Player 2 picks Stravinsky
    ('Stravinsky', 'Bach'): (0, 0),  # Player 1 picks Stravinsky, Player 2 picks Bach
    ('Stravinsky', 'Stravinsky'): (1, 2)  # Both pick Stravinsky
}


choices = ['Bach', 'Stravinsky']


def best_response(payoff_matrix, player, opponent_action):
    """
    Find the best choice(s) for a player, given the opponent's choice.
    payoff_matrix: The dictionary with the payoff table.
    player: 1 (Player 1) or 2 (Player 2).
    opponent_action: What the other player picks ('Bach' or 'Stravinsky').
    Returns: A set of the best choices, like {'Bach'}.
    """
    best_choices = set()  # To store the best choices
    best_points = -1      # Start with a low number to track the highest points

    # Loop through all possible choices for the player
    for my_choice in choices:
        # Get the points for this choice
        if player == 1:
            # Player 1's choice is first, opponent's (Player 2) is second
            pair = (my_choice, opponent_action)
            my_points = payoff_matrix[pair][0]  # First number is Player 1's points
        else:
            # Player 2's choice is second, opponent's (Player 1) is first
            pair = (opponent_action, my_choice)
            my_points = payoff_matrix[pair][1]  # Second number is Player 2's points

        # Check if this choice gives more points than what we've seen
        if my_points > best_points:
            best_choices = {my_choice}  # This is the new best choice
            best_points = my_points     # Update the best points
        elif my_points == best_points:
            best_choices.add(my_choice)  # Add this choice (tied for best)

    return best_choices

# Test the example: Player 1's best response when Player 2 picks 'Bach'
print("Player 1's best response when Player 2 picks 'Bach':", 
      best_response(payoffs, 1, 'Bach'))

# Let's test a few more cases to make sure it works
print("Player 1's best response when Player 2 picks 'Stravinsky':", 
      best_response(payoffs, 1, 'Stravinsky'))
print("Player 2's best response when Player 1 picks 'Bach':", 
      best_response(payoffs, 2, 'Bach'))
print("Player 2's best response when Player 1 picks 'Stravinsky':", 
      best_response(payoffs, 2, 'Stravinsky'))