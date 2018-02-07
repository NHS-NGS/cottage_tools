---
  Modules:
  - return_json
  - return_ir
---
{% for module in page.Modules %}
# {{ module }}
{% capture my_include %}{% include_relative docs/{{ module }}.md %}{% endcapture %}
{{ my_include | markdownify }}
{% endfor %}
