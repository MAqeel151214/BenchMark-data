import numpy as np
from numpy.polynomial import polynomial as P

print("=== TASK 1: MINIMUM VARIANCE PORTFOLIO ===")
Sigma1 = np.array([[0.04, 0.018, 0.012],
                   [0.018, 0.09, 0.048],
                   [0.012, 0.048, 0.16]])
mu1 = np.array([0.08, 0.12, 0.15])
ones = np.ones(3)

inv_Sigma1 = np.linalg.inv(Sigma1)
w1 = inv_Sigma1 @ ones / (ones @ inv_Sigma1 @ ones)
var1 = w1 @ Sigma1 @ w1
ret1 = w1 @ mu1

print(f"Weights: {w1}")
print(f"Sum weights: {np.sum(w1)}")
print(f"Portfolio variance: {var1}")
print(f"Portfolio std dev: {np.sqrt(var1)}")
print(f"Portfolio expected return: {ret1}")

print("\n=== TASK 5: DCF WITH CIRCULAR WACC ===")
# FCFs (in millions)
fcfs = np.array([75.011, 89.038, 103.713, 110.07, 115.729])
tv = 2183.04  # exit multiple terminal value
debt = 380  # market value of debt
shares = 45  # millions
beta = 1.25
rf = 0.045
mrp = 0.055
rd = 0.065
tax = 0.21
re = rf + beta * mrp
print(f"Cost of equity: {re:.4f}")
print(f"After-tax cost of debt: {rd*(1-tax):.4f}")

def compute_price(guess_price):
    equity = guess_price * shares
    v = equity + debt
    ev_ratio = equity / v
    dv_ratio = debt / v
    wacc = ev_ratio * re + dv_ratio * rd * (1 - tax)
    
    pv_fcf = sum(fcfs[i] / ((1+wacc)**(i+1)) for i in range(5))
    pv_tv = tv / ((1+wacc)**5)
    ev = pv_fcf + pv_tv
    implied_equity = ev - debt
    implied_price = implied_equity / shares
    return wacc, ev, implied_price

for guess in [50, 30, 29.8, 29.83]:
    wacc, ev, price = compute_price(guess)
    print(f"Guess ${guess}: WACC={wacc:.4%}, EV=${ev:.2f}M, Implied P=${price:.2f}")

# Find precise solution using iteration
price = 30.0
for i in range(100):
    wacc, ev, new_price = compute_price(price)
    if abs(new_price - price) < 0.0001:
        print(f"Converged at iteration {i}: P=${new_price:.4f}, WACC={wacc:.4%}")
        break
    price = new_price

# Also compute with target capital structure (for comparison)
target_wacc = 0.70 * re + 0.30 * rd * (1 - tax)
pv_fcf_target = sum(fcfs[i] / ((1+target_wacc)**(i+1)) for i in range(5))
pv_tv_target = tv / ((1+target_wacc)**5)
ev_target = pv_fcf_target + pv_tv_target
print(f"If using target D/V=30%: WACC={target_wacc:.4%}, EV=${ev_target:.2f}M")

print("\n=== TASK 7: PARAMETRIC VaR/CVaR ===")
w7 = np.array([0.40, 0.35, 0.25])
mu7 = np.array([0.008, 0.012, 0.015])
Sigma7 = np.array([[0.0016, 0.0006, 0.0004],
                   [0.0006, 0.0025, 0.0008],
                   [0.0004, 0.0008, 0.0036]])
port_mu = w7 @ mu7
port_var = w7 @ Sigma7 @ w7
port_std = np.sqrt(port_var)
print(f"Portfolio expected return: {port_mu:.6f}")
print(f"Portfolio variance: {port_var:.6f}")
print(f"Portfolio std dev: {port_std:.6f}")

z_99 = 2.326347874
var_pct = port_mu - z_99 * port_std
cvar_pct = port_mu - (1/np.sqrt(2*np.pi) * np.exp(-z_99**2/2)) / 0.01 * port_std
print(f"99% VaR (absolute, %): {-var_pct:.6f}")
print(f"99% CVaR (absolute, %): {-cvar_pct:.6f}")
print(f"99% VaR ($50M): ${-var_pct * 50_000_000:,.0f}")
print(f"99% CVaR ($50M): ${-cvar_pct * 50_000_000:,.0f}")

print("\n=== TASK 8: MAXIMUM SHARPE RATIO ===")
# Let's try 3 assets first
mu8 = np.array([0.08, 0.12, 0.16])
Sigma8 = np.array([[0.0225, 0.009, 0.0084],
                   [0.009, 0.04, 0.028],
                   [0.0084, 0.028, 0.0784]])
rf8 = 0.04
excess = mu8 - rf8
inv_Sigma8 = np.linalg.inv(Sigma8)
w8 = inv_Sigma8 @ excess / (np.ones(3) @ inv_Sigma8 @ excess)
ret8 = w8 @ mu8
var8 = w8 @ Sigma8 @ w8
std8 = np.sqrt(var8)
sharpe8 = (ret8 - rf8) / std8

print(f"Weights: {w8}")
print(f"Sum: {np.sum(w8)}")
print(f"Expected return: {ret8:.4f}")
print(f"Std dev: {std8:.4f}")
print(f"Sharpe ratio: {sharpe8:.4f}")

# Also compute Sharpe of equal-weighted for comparison
w_eq = np.array([1/3, 1/3, 1/3])
ret_eq = w_eq @ mu8
std_eq = np.sqrt(w_eq @ Sigma8 @ w_eq)
sharpe_eq = (ret_eq - rf8) / std_eq
print(f"Equal weight return: {ret_eq:.4f}, std: {std_eq:.4f}, Sharpe: {sharpe_eq:.4f}")
