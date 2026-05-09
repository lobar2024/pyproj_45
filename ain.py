class LoanCalculator:
    def __init__(self, principal, annual_rate, months):
        self.principal    = principal
        self.monthly_rate = annual_rate / 100 / 12
        self.months       = months

    def monthly_payment(self):
        r, n = self.monthly_rate, self.months
        if r == 0: return self.principal / n
        return self.principal * r * (1+r)**n / ((1+r)**n - 1)

    def total_payment(self):
        return self.monthly_payment() * self.months

    def total_interest(self):
        return self.total_payment() - self.principal

    def schedule(self, show=6):
        payment = self.monthly_payment()
        balance = self.principal
        print(f"\n{'Oy':>4} {'To\'lov':>12} {'Foiz':>12} {'Asosiy':>12} {'Qoldiq':>14}")
        print("-" * 58)
        for month in range(1, self.months+1):
            interest  = balance * self.monthly_rate
            principal = payment - interest
            balance  -= principal
            if month <= show or month == self.months:
                print(f"{month:>4} {payment:>12,.0f} {interest:>12,.0f} "
                      f"{principal:>12,.0f} {max(0,balance):>14,.0f}")
            elif month == show+1:
                print("  ...")

if __name__ == "__main__":
    loan = LoanCalculator(
        principal   = 50_000_000,
        annual_rate = 24,
        months      = 12
    )
    print(f"Oylik to'lov  : {loan.monthly_payment():,.0f} so'm")
    print(f"Jami to'lov   : {loan.total_payment():,.0f} so'm")
    print(f"Jami foiz     : {loan.total_interest():,.0f} so'm")
    loan.schedule(show=3)
