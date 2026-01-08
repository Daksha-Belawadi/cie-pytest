from bank import bank_details

def test_bank_details():
        expected_output = (
            "Account_number = 515\n"
            "Account_holder_name = Daksha\n"
            "Account_type = Current\n"
            "Balance = 50000\n"
        )
        assert bank_details (515,"Daksha","Current",50000) == expected_output

