---
  Modules:
  - docs/test.md
---
{% for module in page.Modules %}
<p>{% include_relative {{ module }} %}</p> 
{% endfor %}
