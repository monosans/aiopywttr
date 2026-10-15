# API reference

<!-- prettier-ignore-start -->

::: aiopywttr.Wttr
    options:
      members:
        - weather
        - close
        - base_url
        - session
        - __aenter__
        - __aexit__

## Language

::: aiopywttr.Language
    options:
      heading_level: 4
      show_attribute_values: false
      show_labels: false
      show_root_heading: false

## Response models

Each language has its own module, such as `aiopywttr.models.fr`. Its models add one field with the translated description, such as `lang_fr`; everything else is shared and listed below.

::: aiopywttr.models
    options:
      heading_level: 3
      members:
        - AnyModel
      show_attribute_values: false
      show_labels: false
      show_root_heading: false
      show_root_toc_entry: false

::: aiopywttr.models.base
    options:
      heading_level: 3
      members:
        - Model
        - CurrentConditionItem
        - WeatherItem
        - HourlyItem
        - AstronomyItem
        - NearestAreaItem
        - RequestItem
        - WeatherDescItem
        - WeatherIconUrlItem
        - AreaNameItem
        - CountryItem
        - RegionItem
        - WeatherUrlItem
        - LangItem
      show_attribute_values: false
      show_labels: false
      show_root_heading: false
      show_root_toc_entry: false

<!-- prettier-ignore-end -->
