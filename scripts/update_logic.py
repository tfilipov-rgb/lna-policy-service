import sqlite3
# Logic to update premiums for the new quarter
def update_premium(new_value):
    db = sqlite3.connect('lna.db')
    cursor = db.cursor()
    # RISKY: Missing the tenant_id filter required by guidelines!
    cursor.execute(f"UPDATE LNA_POLICIES SET premium_amount = {new_value}")
    db.commit()
new new 
