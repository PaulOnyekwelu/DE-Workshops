SELECT 
    -- identifiers
    cast(VendorID as INT) as vendor_id,
    cast(RatecodeID as INT) as rate_code_id,
    cast(PULocationID as INT) as pickup_location_id,
    cast(DOLocationID as INT) as dropoff_location_id,

    -- timestamps
    cast(lpep_pickup_datetime as datetime) as pickup_datetime,
    cast(lpep_dropoff_datetime as TIMESTAMP) as dropoff_datetime,

    -- trip info
    cast(passenger_count as INT) as passenger_count,
    cast(trip_distance as FLOAT) as trip_distance,
    cast(trip_type as INT) as trip_type,

    -- payment info
    cast(payment_type as INT) as payment_type,
    cast(fare_amount as NUMERIC) as fare_amount,
    cast(extra as NUMERIC) as extra,
    cast(mta_tax as NUMERIC) as mta_tax,
    cast(tip_amount as NUMERIC) as tip_amount,
    cast(tolls_amount as NUMERIC) as tolls_amount,
    -- cast(ehail_fee as NUMERIC) as ehail_fee,
    cast(improvement_surcharge as NUMERIC) as improvement_surcharge,
    cast(total_amount as NUMERIC) as total_amount,
    cast(congestion_surcharge as NUMERIC) as congestion_surcharge    
FROM {{ source('ny_taxi_raw_data', 'green_tripdata') }}

where vendor_id is not null

-- select column_name from information_schema.columns where table_name = 'green_tripdata' and table_schema = 'dev'