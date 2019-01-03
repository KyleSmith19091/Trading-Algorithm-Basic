#Init Runs once i.e. when the script is run
def initialize(context):
    #Stock ID -- sid
    context.appl = sid(16841) 
    schedule_function(ma_crossover_handling, date_rules.every_day(), time_rules.market_open(hours=1))
    
def ma_crossover_handling(context, data):    
     #hist - hisotry, price -- field, how many sets of data?, 1d -- 1 day
    hist = data.history(context.appl, 'price', 50, '1d')
    log.info(hist.head())
    sma_50 = hist.mean()
    sma_20 = hist[-20:].mean()
    
    open_orders = get_open_orders()
    
    #100% of portfolio will be apple
    if sma_20 > sma_50:
        if context.appl not in open_orders:
            order_target_percent(context.appl, 1.0)
    elif sma_50 > sma_20:
    # Short Apple -- Risky
        if context.appl not in open_orders:
            order_target_percent(context.appl, -1.0)
        
    record(leverage = context.account.leverage)
