{% extends "frontend/base_site.tpl" %}
{% block content %}
<h1>{{ poll.question }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="/polls/{{ poll.id }}/vote/" method="post">
{% csrf_token %}
{% for choice in poll.choice_set.all %}
    <input class="input" type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label class="input" for="choice{{ forloop.counter }}">{{ choice.choice }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>
{% endblock %}