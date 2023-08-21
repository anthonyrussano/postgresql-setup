SELECT
    EXISTS (
        SELECT
        FROM
            PG_TABLES
        WHERE
            TABLENAME LIKE '%table_name%'
    );