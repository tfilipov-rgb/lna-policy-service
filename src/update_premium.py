# src/update_premium.py

import psycopg2

def update_premium(conn, new_amount):
    with conn.cursor() as cur:
        # Intentional policy violation: missing tenant_id filter!
        cur.execute("""
            UPDATE premiums
            SET amount = %s
            WHERE policy_status = 'active'
        """, (new_amount,))
    conn.commit()
