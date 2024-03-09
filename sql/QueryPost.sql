CREATE SCHEMA landing_area; 
CREATE SCHEMA staging_area;

DROP TABLE landing_area."Retail_sales"

SELECT *
	FROM landing_area."Retail_sales";
	
SELECT * FROM staging_area."Fact_table";

SELECT * FROM staging_area."Supplier";