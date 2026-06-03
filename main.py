from biometric_auth import (
    detect_live_face,
    windows_hello_auth
)


class Bank:

    def __init__(self, owner, acc_no, pin, balance=0):

        self.owner = owner
        self.acc_no = acc_no
        self.pin = pin
        self.balance = balance
        self.logged_in = False

        # FD Details
        self.fd_amount = 0
        self.fd_years = 0
        self.fd_interest = 7


    # ---------------- REALTIME BIOMETRIC LOGIN ---------------- #

    def biometric_login(self):

        print('\n===== REALTIME BIOMETRIC AUTH =====')

        # STEP 1 - FACE DETECTION
    
        face_verified = detect_live_face()

        if face_verified:
           
            # STEP 2 - WINDOWS HELLO
            hello_verified = windows_hello_auth()

            if hello_verified:

                self.logged_in = True

                print(f'\nWelcome {self.owner}')
                print('Biometric Authentication Successful')
### sdnkgsbgisbgsibv
                return True

        print('\nBiometric Authentication Failed')

        return False
     # ---------------- PIN LOGIN ---------------- #

    def pin_login(self):

        entered_acc = input('Enter Account Number: ')
        entered_pin = input('Enter PIN: ')

        if (
            entered_acc == self.acc_no and
            entered_pin == self.pin
        ):

            self.logged_in = True

            print(f'\nWelcome {self.owner}')
            print('PIN Login Successful')

            return True

        else:

            print('Invalid Account Number or PIN')

            return False


    # ---------------- DEPOSIT ---------------- #

    def deposit(self):

        amt = int(input('Enter amount to deposit: '))

        if amt > 0:

            self.balance += amt

            print(f'{amt} deposited successfully')
            print('Current Balance:', self.balance)

        else:

            print('Invalid Amount')

     # ---------------- WITHDRAW ---------------- #

    def withdraw(self):

        amt = int(input('Enter amount to withdraw: '))

        if amt > self.balance:

            print('Insufficient Balance')

        else:

            self.balance -= amt

            print(f'{amt} withdrawn successfully')
            print('Remaining Balance:', self.balance)


    # ---------------- BALANCE CHECK ---------------- #

    def check_balance(self):

        print('Current Balance:', self.balance)


    # ---------------- CREATE FD ---------------- #

    def fixed_deposit(self):

        if self.fd_amount > 0:

            print('FD already exists')
            return

        amt = int(input('Enter FD Amount: '))

        if amt > self.balance:

            print('Insufficient Balance')

        else:

            years = int(input('Enter FD Years: '))

            self.balance -= amt

            self.fd_amount = amt
            self.fd_years = years

            maturity = amt + (
                amt * self.fd_interest * years
            ) / 100

            print('\nFD Created Successfully')
            print('Maturity Amount:', maturity)
            print('Remaining Saving Balance:', self.balance) 

    # ---------------- SHOW FD ---------------- #

    def show_fd(self):

        if self.fd_amount == 0:

            print('No Active FD')

        else:

            maturity = self.fd_amount + (
                self.fd_amount * self.fd_interest * self.fd_years
            ) / 100

            print('\n===== FD DETAILS =====')

            print('FD Amount:', self.fd_amount)
            print('Years:', self.fd_years)
            print('Interest:', self.fd_interest, '%')
            print('Maturity Amount:', maturity) 

    # ---------------- CLOSE FD ---------------- #

    def close_fd(self):

        if self.fd_amount == 0:

            print('No Active FD Found')
            return

        print('\nClosing FD Before Maturity')

        penalty = (self.fd_amount * 2) / 100

        returned_amount = self.fd_amount - penalty

        self.balance += returned_amount

        print('Penalty Charged:', penalty)
        print('Returned Amount:', returned_amount)

        self.fd_amount = 0
        self.fd_years = 0

user = Bank(
owner='Krish',
acc_no='1001',
pin='1234',
balance=50000
)
# ---------------- MAIN SYSTEM ---------------- #
while True:
    print('\n===== BANKING SYSTEM =====')

    print('1. Realtime Biometric Login')
    print('2. Account Number + PIN Login')
    print('3. Exit')

    choice = input('\nEnter Choice: ')

# ---------------- BIOMETRIC LOGIN ---------------- #

    if choice == '1':
        success = user.biometric_login()
        if success:
            while True:
                print('\n===== BANK MENU =====')
                print('1. Deposit')
                print('2. Withdraw')
                print('3. Check Balance')
                print('4. Create FD')
                print('5. Show FD')
                print('6. Close FD')
                print('7. Logout')

                option = input('\nChoose Option: ')
                
                if option == '1':
                     user.deposit()
              
                elif option == '2':
                    user.withdraw()

                elif option == '3':   
                    user.check_balance()

                elif option == '4':
                    user.fixed_deposit()

                elif option == '5':
                    user.show_fd()

                elif option == '6':
                    user.close_fd()

                elif option == '7':
                    print('Logged Out Successfully')
                    break
                else:
                    print('Invalid Choice') 

                    

        else:
            print('\nFalling Back To PIN Login')
            pin_success = user.pin_login()

            if pin_success:

                while True:

                    print('\n===== BANK MENU =====')

                    print('1. Deposit')
                    print('2. Withdraw')
                    print('3. Check Balance')
                    print('4. Create FD')
                    print('5. Show FD')
                    print('6. Close FD')
                    print('7. Logout')

                    option = input('\nChoose Option: ')
                    
                    if option == '1':
                        user.deposit()
                
                    elif option == '2':
                        user.withdraw()

                    elif option == '3':   
                        user.check_balance()

                    elif option == '4':
                        user.fixed_deposit()

                    elif option == '5':
                        user.show_fd()

                    elif option == '6':
                        user.close_fd()

                    elif option == '7':
                        print('Logged Out Successfully')
                        break
                    else:
                        print('Invalid Choice') 
                    

    elif choice =='2':
        sucess = user.pin.login()

        if success:

            while True:

                    print('\n===== BANK MENU =====')

                    print('1. Deposit')
                    print('2. Withdraw')
                    print('3. Check Balance')
                    print('4. Create FD')
                    print('5. Show FD')
                    print('6. Close FD')
                    print('7. Logout')

                    option = input('\nChoose Option: ')
                    
                    if option == '1':
                        user.deposit()
                
                    elif option == '2':
                        user.withdraw()

                    elif option == '3':   
                        user.check_balance()

                    elif option == '4':
                        user.fixed_deposit()

                    elif option == '5':
                        user.show_fd()

                    elif option == '6':
                        user.close_fd()

                    elif option == '7':
                        print('Logged Out Successfully')
                        break
                    else:
                        print('Invalid Choice') 
                    
    elif choice=='3':
        
        print("thank you for using banking system")
        break
    
    else:
        print("invalid choice ")                



          

     
                    

