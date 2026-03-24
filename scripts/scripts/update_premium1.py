import sqlite3
def update_premium(val):
    conn = sqlite3.connect('lna.db')
    # VIOLATION: Missing 'where tenant_id = ?'
    conn.execute(f"UPDATE LNA_POLICIES SET premium_amount = {val}") 
