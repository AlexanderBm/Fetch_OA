transactions = []
balances = {}

def add_transaction(payer, points, timestamp):
    transactions.append({'payer': payer, 'points': points, 'timestamp': timestamp})
    balances[payer] = balances.get(payer, 0) + points

def spend_points(points_to_spend):
    if sum(balances.values()) < points_to_spend:
        return "Not enough points", 400

    transactions.sort(key=lambda x: x['timestamp'])
    spent_points = []
    remaining_points = points_to_spend

    for transaction in transactions:
        if remaining_points == 0:   
            break

        payer = transaction['payer']
        points_to_deduct = min(transaction['points'], remaining_points)
        transaction['points'] -= points_to_deduct
        balances[payer] -= points_to_deduct
        remaining_points -= points_to_deduct
        spent_points.append({'payer': payer, 'points': -points_to_deduct})

    transactions[:] = [t for t in transactions if t['points'] != 0]
    return spent_points, 200

def get_balances():
    return balances