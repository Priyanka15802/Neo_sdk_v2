"""
    Add the settings related information in the given file
"""

UAT_URL = {
    "view_token": "api/1.0/login/v2/validate",
    "generate_otp": "api/1.0/login/otp/generate",
    "edit_token": "api/1.0/login/v2/validate",
    "place_order": "orderapi/1.0/quick/order/rule/ms/place",
    "cancel_order": "orderapi/1.0/quick/order/cancel",
    "modify_order": "orderapi/1.0/quick/order/vr/modify",
    "order_history": "orderapi/1.0/quick/order/history",
    "order_book": "orderapi/1.0/quick/user/orders",
    "trade_report": "orderapi/1.0/quick/user/trades",
    "positions": "orderapi/1.0/quick/user/positions",
    "holdings": "portfolio/1.0/portfolio/v1/holdings",
    "margin": "orderapi/1.0/quick/user/check-margin",
    "scrip_master": "scrip/1.0/masterscrip/file-paths",
    "limits": "orderapi/1.0/quick/user/limits",
    "logout": "api/1.0/logout",
    "base_url": "algo-user/v5/get-base-url",
    "totp_verify_user": "api/1.0/login/v6/totp/verify-user",
    "totp_registration": "api/1.0/login/v6/totp/register",
    "totp_login": "api/1.0/login/v6/totp/login",
    "totp_validate": "api/1.0/login/v6/totp/validate",
    "totp_de_register": "apim/login/2.0/login/v6/totp/deregister",
    "quotes_neo_symbol": "apim/quotes/2.0/quotes/neosymbol/{neo_symbols}/{quote_type}",
    "qr_code_get_link": "apim/login/2.0/algo-user/v5/login/authorization/dialog",
    "qr_code_generate_session": "apim/login/2.0/algo-user/v5/login/generate-session-token"
}

PROD_URL = {
    "view_token": "apim/login/2.0/login/v2/validate",
    "generate_otp": "apim/login/2.0/login/otp/generate",
    "edit_token": "apim/login/2.0/login/v2/validate",
    "place_order": "apim/orders/2.0/quick/order/rule/ms/place",
    "place_order_napi": "Orders/2.0/quick/order/rule/ms/place",
    "cancel_order": "apim/orders/2.0/quick/order/cancel",
    "cancel_order_napi": "Orders/2.0/quick/order/cancel",
    "cancel_cover_order": "apim/orders/2.0/quick/order/co/exit",
    "cancel_cover_order_napi": "Orders/2.0/quick/order/co/exit",
    "cancel_bracket_order": "apim/orders/2.0/quick/order/bo/exit",
    "cancel_bracket_order_napi": "Orders/2.0/quick/order/bo/exit",
    "modify_order": "apim/orders/2.0/quick/order/vr/modify",
    "modify_order_napi": "Orders/2.0/quick/order/vr/modify",
    "order_history": "apim/order/2.0/quick/order/history",
    "order_history_napi": "Orders/2.0/quick/order/history",
    "order_book": "apim/orders/2.0/quick/user/orders",
    "order_book_napi": "Orders/2.0/quick/user/orders",
    "trade_report": "apim/orders/2.0/quick/user/trades",
    "trade_report_napi": "Orders/2.0/quick/user/trades",
    "positions": "apim/orders/2.0/quick/user/positions",
    "positions_napi": "Orders/2.0/quick/user/positions",
    "holdings": "apim/portfolio/2.0/portfolio/v1/holdings",
    "holdings_napi": "Portfolio/1.0/portfolio/v1/holdings",
    "margin": "apim/orders/2.0/quick/user/check-margin",
    "margin_napi": "Orders/2.0/quick/user/check-margin",
    "scrip_master": "apim/files/2.0/masterscrip/v1/file-paths",
    "scrip_master_napi": "Files/1.0/masterscrip/v2/file-paths",
    "limits": "apim/orders/2.0/quick/user/limits",
    "limits_napi": "Orders/2.0/quick/user/limits",
    "logout": "apim/login/2.0/logout",
    "base_url": "algo-user/v5/get-base-url",
    "totp_verify_user": "apim/login/2.0/login/v6/totp/verify-user",
    "totp_registration": "apim/login/2.0/login/v6/totp/register",
    "totp_login": "apim/login/2.0/login/v6/totp/login",
    "totp_login_napi": "login/1.0/login/v6/totp/login",
    "totp_validate": "apim/login/2.0/login/v6/totp/validate",
    "totp_validate_napi": "login/1.0/login/v6/totp/validate",
    "totp_de_register": "apim/login/2.0/login/v6/totp/deregister",
    "quotes_neo_symbol": "apim/quotes/2.0/quotes/neosymbol/{neo_symbols}/{quote_type}",
    "quotes_neo_symbol_napi": "apim/quotes/1.0/quotes/neosymbol/{neo_symbols}/{quote_type}",
    "qr_code_get_link": "apim/login/2.0/algo-user/v5/login/authorization/dialog",
    "qr_code_get_link_napi": "login/1.0/algo-user/v5/login/authorization/dialog",
    "qr_code_generate_session": "apim/login/2.0/algo-user/v5/login/generate-session-token",
    "qr_code_generate_session_napi": "login/1.0/algo-user/v5/login/generate-session-token"
}

exchange_segment_allowed_values = ["NSE", "nse", "BSE", "bse", "NFO", "nfo", "BFO", "bfo", "CDS", "cds", "BCD", "bcd",
                                   "nse_cm", "bse_cm", "nse_fo", "bse_fo", "cde_fo", "bcs-fo"]

product_allowed_values = ["NRML", "CNC", "MIS", "INTRADAY", "CO", "BO", "Normal", "Cash and Carry", "Cover Order",
                          "Bracket Order"]

order_type_allowed_values = ["Limit", "Market", "Stop loss limit", "Stop loss market", "Spread", "Two Leg", "Three leg",
                             "L", "MKT", "SL", "SL-M", "SP", "2L", "3L"]

exchange_segment = {"nse_cm": "nse_cm", "NSE": "nse_cm", "nse": "nse_cm", "BSE": "bse_cm", "bse": "bse_cm",
                    "bse_cm": "bse_cm", "NFO": "nse_fo", "nse_fo": "nse_fo", "nfo": "nse_fo", "BFO": "bse_fo",
                    "bse_fo": "bse_fo", "bfo": "bse_fo", "CDS": "cde_fo", "cde_fo": "cde_fo", "cds": "cde_fo",
                    "BCD": "bcs-fo", "bcs-fo": "bcs-fo", "bcd": "bcs-fo",  "MCX": "mcx", "mcx": "mcx", "mcx_fo": "mcx"}

product = {"Normal": "NRML", "NRML": "NRML", "CNC": "CNC", "cnc": "CNC", "Cash and Carry": "CNC", "MIS": "MIS",
           "mis": "MIS", "INTRADAY": "INTRADAY", "intraday": "INTRADAY", "Cover Order": "CO", "co": "CO",
           "CO": "CO", "BO": "BO", "Bracket Order": "BO", "bo": "BO"}

order_type = {"Limit": "L", "L": "L", "l": "L", "MKT": "MKT", "mkt": "MKT", "Market": "MKT", "sl": "SL", "SL": "SL",
              "Stop loss limit": "SL", "Stop loss market": "SL-M", "SL-M": "SL-M", "sl-m": "SL-M", "Spread": "SP",
              "SP": "SP", "sp": "SP", "2L": "2L", "2l": "2L", "Two Leg": "2L", "3L": "3L", "3l": "3L",
              "Three leg": "3L"}

segment_limits = ["CASH", "CUR", "FO", "ALL"]
exchange_limits = ["NSE", "BSE", "ALL"]
product_limits = ["CNC", "MIS", "NRML", "ALL"]

stock_key_mapping = {
    'ltt': "last_traded_time",
    'v': "volume",
    'ltp': "last_traded_price",
    'ltq': "last_traded_quantity",
    'tbq': "total_buy_quantity",
    'tsq': "total_sell_quantity",
    'bp': "buy_price",
    'sp': "sell_price",
    'bq': "buy_quantity",
    'sq': "sell_quantity",
    'ap': "average_price",
    'oi': "open_interest",
    'lo': "low",
    'h': "high",
    'lcl': "lower_circuit_limit",
    'ucl': "upper_circuit_limit",
    'yh': "52week_high",
    'yl': "52week_low",
    'op': "open",
    'c': "close",
    'mul': "multiplier",
    'prec': "precision",
    'cng': "change",
    'nc': "net_change_percentage",
    'to': "total_traded_value",
    'tk': "instrument_token",
    'e': "exchange_segment",
    'ts': "trading_symbol",
    'request_type':"request_type"
}

index_key_mapping = {
    "iv": "last_traded_price",
    "ic": "prev_day_close",
    "tvalue": "timestamp",
    "highPrice": "high_price",
    "lowPrice": "low_price",
    "openingPrice": "open",
    "mul": "multiplier",
    "prec": "precision",
    "cng": "change",
    "nc": "net_change_percentage",
    "tk": "instrument_token",
    "e": "exchange_segment"
}

MarketDepthResp = {'depth': {}}
MarketDepthResp['depth']['buy'] = [{"price": "", "quantity": "", "orders": ""},
                                   {"price": "", "quantity": "", "orders": ""},
                                   {"price": "", "quantity": "", "orders": ""},
                                   {"price": "", "quantity": "", "orders": ""},
                                   {"price": "", "quantity": "", "orders": ""}]
MarketDepthResp['depth']['sell'] = [{"price": "", "quantity": "", "orders": ""},
                                    {"price": "", "quantity": "", "orders": ""},
                                    {"price": "", "quantity": "", "orders": ""},
                                    {"price": "", "quantity": "", "orders": ""},
                                    {"price": "", "quantity": "", "orders": ""}]

ReqTypeValues = {
    "CONNECTION": "cn",
    "SCRIP_SUBS": "mws",
    "SCRIP_UNSUBS": "mwu",
    "INDEX_SUBS": "ifs",
    "INDEX_UNSUBS": "ifu",
    "DEPTH_SUBS": "dps",
    "DEPTH_UNSUBS": "dpu",
    "CHANNEL_RESUME": "cr",
    "CHANNEL_PAUSE": "cp",
    "SNAP_MW": "mwsp",
    "SNAP_DP": "dpsp",
    "SNAP_IF": "ifsp",
    "OPC_SUBS": "opc",
    "THROTTLING_INTERVAL": "ti",
    "STR": "str",
    "FORCE_CONNECTION": "fcn"
}

#neo_fin_key = "f784e198-bda7-439e-a1a6-177f432460b9"
#neo_fin_key = "bQJNkL5z8m4aGcRgjDvXhHfSx7VpZnE"
#live_fin_key = "neotradeapi"
#live_fin_key = "X6Nk8cQhUgGmJ2vBdWw4sfzrz4L5En"
market_protection = 0
QuotesChannel = 1

help_functions = {
    1: 'help("place_order")',
    2: 'help("modify_order")',
    3: 'help("holdings")',
    4: 'help("positions")',
    5: 'help("limits")',
    6: 'help("trade_report")',
    7: 'help("margin_required")',
    8: 'help("cancel_order")',
    9: 'help("order_history")',
    10: 'help("scrip_master")',
    11: 'help("quotes")',
    12: 'help("socket")',
    13: 'help("search_scrip")',
    14: 'help("order_report")',
    15: 'help("subscribe_to_orderfeed")',
    16: 'help()'
}

ORDER_SOURCE = 'NEOFINTECH001'