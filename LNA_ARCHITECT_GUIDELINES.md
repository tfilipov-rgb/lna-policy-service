# LNA Architecture Rules
1. All SQL 'UPDATE' statements MUST include a 'WHERE' clause filtering by 'tenant_id'.
2. Never hardcode API keys in the source code.
3. All database changes require a corresponding rollback script.
