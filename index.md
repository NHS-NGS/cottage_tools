---
  Modules:
  - docs/return_json.md
  - docs/return_ir.md
---
{% for module in page.Modules %}
{% capture my_include %}{% include_relative {{ module }} %}{% endcapture %}
{{ my_include | markdownify }}
{% endfor %}
