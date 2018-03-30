#  -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import seaborn

# Fortis stock price 
spot_price = 138.90

# Long put
strike_price_long_put = 135
premium_long_put = 4

# Long call
strike_price_long_call = 145 
premium_long_call = 3.50

#CallPutRatio = 3.0
CallPutRatio = 0.5

# Stock price range at expiration of the put
sT = np.arange(0.5*spot_price,1.5*spot_price,1)

def call_payoff(sT, strike_price, premium):
    return (np.where(sT > strike_price, sT - strike_price, 0)-premium)

payoff_long_call = call_payoff(sT, strike_price_long_call, premium_long_call)
payoff_short_call = -call_payoff(sT, strike_price_long_call, premium_long_call)

# Plot
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_long_call,label='Long Call',color='r')
ax.plot(sT,payoff_short_call,label='Short Call',color='y')
plt.xlabel('Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()



def put_payoff(sT, strike_price, premium):
    return np.where(sT < strike_price, strike_price - sT, 0)-premium
      
payoff_long_put = put_payoff(sT, strike_price_long_put, premium_long_put)
payoff_short_put = -put_payoff(sT, strike_price_long_put, premium_long_put)

# Plot
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_long_put,label='Long Put',color='g')
ax.plot(sT,payoff_short_put,label='Short Put',color='b')
plt.xlabel('Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()


payoff_strangle = CallPutRatio*payoff_long_call + payoff_long_put

print ("Max Profit for Long: Unlimited")
print ("Max Loss for Long:", min(payoff_strangle))

# Plot
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')

ax.plot(sT,payoff_long_call,'--',label='Long Call',color='r')
ax.plot(sT,payoff_long_put,'--',label='Long Put',color='g')

ax.plot(sT,payoff_strangle,label='Strangle')
plt.xlabel('Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()

payoff_strangle = CallPutRatio*payoff_short_call + payoff_short_put

print ("Max Loss for Short: Unlimited")
print ("Max Profit for Short:", max(payoff_strangle))

# Plot
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')

ax.plot(sT,payoff_short_call,'--',label='Short Call',color='y')
ax.plot(sT,payoff_short_put,'--',label='Short Put',color='b')

ax.plot(sT,payoff_strangle,label='Strangle')
plt.xlabel('Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()
