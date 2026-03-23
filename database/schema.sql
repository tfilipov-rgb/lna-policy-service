CREATE TABLE LNA_POLICIES (
    policy_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    premium_amount DECIMAL(10,2),
    tenant_id INT NOT NULL
);
