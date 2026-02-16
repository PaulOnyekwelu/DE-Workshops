WITH unique_vendor_ids AS (
    SELECT DISTINCT vendor_id FROM {{ ref('int_trips_unioned') }}
),
vendors AS (
    SELECT 
        vendor_id,
        {{ get_vendor_names('vendor_id') }} AS vendor_name
    FROM unique_vendor_ids
)

SELECT * FROM vendors