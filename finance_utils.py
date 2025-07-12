def dcf(FreeCashFlow, growth_rate, discount_rate, years = 5, terminal_growth = 0.02):
    '''
    Args := 
        - FreeCashFlow: the (current) free cash flow
        - growth rate: annual growth rate of FCF
        - discount rate: Weighted Average Cost of Capital
        - years: number of forecast years
        - terminal growth: terminal growth rate beyond forecast
    result: estimated intrinsic value based on discounted cash flows
    '''
    total_val = 0
    for t in range(1, years+1):
        projected_fcf = FreeCashFlow*((1+growth_rate)**t)
        discounted_fcf = projected_fcf/((1+discount_rate)**t)
        total_val += discounted_fcf
    
    # term. val. at the end of forecast horizon:
    fcf_terminal = FreeCashFlow * ((1+growth_rate)**years)
    terminal_value = (fcf_terminal * (1+terminal_growth))/(discount_rate - terminal_growth)
    discounted_term_value = terminal_value / ((1+discount_rate)**years)
    total_val += discounted_term_value

    return total_val