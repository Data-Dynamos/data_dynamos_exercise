{% test test_year_column(model, column_name) %}

with data as (
    select
        {{ column_name }} as year_column
    from
        {{ model }}
)

select
    year_column
from
    data
where
    not (regexp_like(year_column, '^[0-9]{4}$'))


{% endtest %}