

def update_balance(debit):
    account = debit.member_account
    current_balance = debit.member_account.balance
    debit_amount = debit.amount

    updated_balance = current_balance + debit_amount
    account.balance = updated_balance
    account.save()
    return updated_balance
