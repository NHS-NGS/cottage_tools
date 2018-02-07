---
  Modules:
  - docs/test.md
---
{% for module in page.Modules %}
{% capture my_include %}{% include_relative {{ module }} %}{% endcapture %}
{{ my_include | markdownify }}
{% endfor %}
