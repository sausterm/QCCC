# Quantum Portfolio Optimization

In this project, we explored using Quantum Computing, specifically the Quantum Approximate Optimization Algorithm (QAOA), to tackle the Portfolio Optimization problem. Our primary goal was to find the optimal combination of stocks that maximizes returns while minimizing risk.

## Background

The Portfolio Optimization problem is a fundamental problem in finance. It involves finding the best way to invest a certain amount of money across a selection of stocks to achieve the maximum return for a given level of risk or to minimize risk for a given level of return.

## Quantum Computing Approach

Quantum Computing promises to provide solutions to problems that are computationally expensive for classical computers. By using QAOA, a quantum computing algorithm, we aimed to find solutions to the Portfolio Optimization problem more efficiently than traditional methods.

## Project Structure

1. **Defining the Portfolio Data**: We used sample data to define expected returns (`r`) and a covariance matrix (`cov_matrix`) for a set of stocks.

2. **Hamiltonian Construction**: We built Hamiltonians (`cost_hamiltonian` and `mixer_hamiltonian`) that represent our problem on a quantum computer.

3. **QAOA Circuit**: We implemented a QAOA circuit that used the constructed Hamiltonians to find the optimal bit string representing the best combination of stocks.

4. **QAOA Sampling**: We take many samples to statistically determine which bit string is most likely the optimal solution. The bit string that appears most frequently in the samples is considered the best approximation to the optimal portfolio combination.



## Results

By iterating through potential solutions, we were able to identify portfolio combinations with high Sharpe ratios, indicating good risk-adjusted returns. 

## Future Work

1. **Real Data Integration**: Integrate real stock market data to make more realistic portfolio decisions.
2. **Extended Quantum Algorithms**: Explore other quantum algorithms for enhanced performance.
3. **Hardware Integration**: Test on actual quantum hardware when available at scale.
4. **Extended Optimization Algorithms**: Explore other opti ization algorithms for faster search of the problem space (LSTM have been applied to similar problems and have worked well).

XchWorLVrfWmusbwBfy8JXCL8QY76o3O0iEGyV