{% macro replace_invalid_chars(column_name) %}
    {% set invalid_chars = [" ", ",", ";", "\n", "\t", "=", "-", "{", "}", "(", ")", "%","$"] %}
    {% set underscore_candidates = [" ", ",", ";", "\n", "\t", "=", "-"] %}
    {% set new_name = column_name %}
    {% set ns = namespace(new_name=new_name) %}

    {% for char in invalid_chars %}
        {% set replacement = "_" if char in underscore_candidates else "" %}
        {% set replacement = "percentage" if char == "%" else replacement %}
        {% set ns.new_name = ns.new_name.replace(char, replacement) %}
    {% endfor %}

    {{ ns.new_name.strip().replace(" ", "_") }}
{% endmacro %}
