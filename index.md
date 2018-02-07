---
  Modules:
  - return_json
  - return_ir
---
{% for module in page.Modules %}
{% capture my_include %}{% include_relative docs/{{ module }}.md %}{% endcapture %}
## {{ module }}
{{ my_include | markdownify }}
{% endfor %}
