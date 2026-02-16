WITH trips_unioned AS (
    SELECT * FROM {{ ref('int_trips_unioned') }}
),
trips_unioned_with_pk AS (
    SELECT 
        -- ROW_NUMBER() OVER (order by pickup_location_id) AS trip_id,
        concat(vendor_id, )
        *
    FROM trips_unioned
)

SELECT * from trips_unioned_with_pk limit 50
