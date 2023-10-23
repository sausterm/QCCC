import json

def generate_portfolio_data(N):
    """
    Generates data for the portfolio optimization problem.
    
    Args:
        N (int): Number of stocks in the portfolio.

    Returns:
        dict: A dictionary containing the generated data.
    """
    # Randomly generate expected returns for each stock
    r = np.random.uniform(0, 1, N)
    
    # Generate the covariance matrix
    cov_matrix = np.random.uniform(-0.01, 0.01, (N, N))
    
    # Ensure it's symmetric
    cov_matrix = (cov_matrix + cov_matrix.T) / 2
    
    # Set the diagonal to represent variances
    np.fill_diagonal(cov_matrix, np.random.uniform(0.01, 0.5, N))
    
    # Calculate A (using a default weighting factor w=0.5 for simplicity)
    w = 0.5
    A = (1-w) * 2 * cov_matrix - w * np.diag(r)
    
    return {
        'r': r,
        'cov_matrix': cov_matrix,
    }




class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):  # Convert numpy arrays
            return obj.tolist()
        if 'tensor' in str(type(obj)):  # Convert tensors (basic assumption, might need adjustment)
            return obj.numpy().tolist()  # Assuming you can convert tensor to numpy
        return super().default(obj)

 

    
def write_json_input(json_obj):

    #json_obj = {'r':r,
    # 'cov_matrix':cov_matrix}
    n = len(json_obj['r'])
    with open(f'QCCC/example_input_n={n}.json', 'w') as json_file:
        json.dump(json_obj, json_file, cls=CustomEncoder)