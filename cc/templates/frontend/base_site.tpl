{% load url from future %}<!DOCTYPE html>
<html lang="{{ LANGUAGE_CODE|default:"en-us" }}" {% if LANGUAGE_BIDI %}dir="rtl"{% endif %}>
<head>
<title>{% block title %}{% endblock %}</title>
{% block extrastyle %}{% endblock %}
{% block blockbots %}<meta name="robots" content="NONE,NOARCHIVE" />{% endblock %}

    <link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}/static/frontend/css/bootstrap.min.css"/>
    
    <script type="text/javascript" src="{{ STATIC_URL }}/static/frontend/js/jquery-1.8.0.min.js"></script>
    <script type="text/javascript" src="{{ STATIC_URL }}/static/frontend/js/bootstrap.min.js"></script>
</head>
{% load i18n %}

<body class="{% if is_popup %}popup {% endif %}{% block bodyclass %}{% endblock %}">
<!-- Container -->
<div id="container">

    {% if not is_popup %}
    <!-- Header -->
    <div id="header">
        <div id="branding">
        {% block branding %}{% endblock %}
        </div>
        {% if user.is_active and user.is_staff %}
        <div id="user-tools">
            {% trans 'Welcome,' %}
            <strong>{% filter force_escape %}{% firstof user.first_name user.username %}{% endfilter %}</strong>.
            {% block userlinks %}
                {% url 'django-admindocs-docroot' as docsroot %}
                {% if docsroot %}
                    <a href="{{ docsroot }}">{% trans 'Documentation' %}</a> /
                {% endif %}
                <a href="{% url 'admin:password_change' %}">{% trans 'Change password' %}</a> /
                <a href="{% url 'admin:logout' %}">{% trans 'Log out' %}</a>
            {% endblock %}
        </div>
        {% endif %}
        {% block nav-global %}{% endblock %}
    </div>
    <!-- END Header -->
    {% block breadcrumbs %}
    <div class="breadcrumbs">
    <a href="{% url 'cc.views.index' %}">{% trans 'Home' %}</a>
    {% if title %} &rsaquo; {{ title }}{% endif %}
    </div>
    {% endblock %}
    {% endif %}

    {% block messages %}
        {% if messages %}
        <ul class="messagelist">{% for message in messages %}
          <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
        {% endfor %}</ul>
        {% endif %}
    {% endblock messages %}

    <!-- Content -->
    <div id="content" class="{% block coltype %}colM{% endblock %}">
        {% block pretitle %}{% endblock %}
        {% block content_title %}{% if title %}<h1>{{ title }}</h1>{% endif %}{% endblock %}
        {% block content %}
        {% block object-tools %}{% endblock %}
        {{ content }}
        {% endblock %}
        {% block sidebar %}{% endblock %}
        <br class="clear" />
    </div>
    <!-- END Content -->

    {% block footer %}<div id="footer" style="text-align: center;">Hosted and Designed by WritheM Web Solutions<br /><a href="http://writhem.com/"><img src="http://billing.writhem.com/images/logo.jpg" /></a></div>{% endblock %}
</div>
<!-- END Container -->

</body>
</html>