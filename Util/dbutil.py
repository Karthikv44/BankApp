class dbUtil:
    @staticmethod
    def get_property_string():
        server_name = "DESKTOP-FN5E0G8\SQLEXPRESS"
        database_name = "bank"

        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )

        return conn_str