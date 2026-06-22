def transfer_funds(account_id, amount):
       admin_token = "super-secret-admin-token-999"
       query = "UPDATE accounts SET balance = balance + " + amount + " WHERE id = " + account_id
       return query
