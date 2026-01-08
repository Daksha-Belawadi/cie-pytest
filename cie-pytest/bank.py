def bank_details(Account_number,Account_holder_name,Account_type,Balance):
    result = (
        f"Account number: {Account_number}\n"
        f"Account holder name: {Account_holder_name}\n"
        f"Account Type: {Account_type}\n"
        f"Balance: {Balance}\n"
    )
    return result

if __name__ == "__main__":
    Account_number="515\n"
    Account_holder_name="Daksha\n"
    Account_type="Current\n"
    Balance="50000\n"
    print(bank_details("Account_number:,Account_holder:,Account_type:,Balance:"))